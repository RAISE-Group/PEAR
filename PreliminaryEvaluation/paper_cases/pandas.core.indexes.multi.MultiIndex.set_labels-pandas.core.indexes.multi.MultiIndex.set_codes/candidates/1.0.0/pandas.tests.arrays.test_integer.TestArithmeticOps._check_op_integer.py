def _check_op_integer(self, result, expected, mask, s, op_name, other):
    fill_value = 0
    if op_name in ['__mod__', '__rmod__']:
        if is_scalar(other):
            if other == 0:
                expected[s.values == 0] = 0
            else:
                expected = expected.fillna(0)
        else:
            expected[(s.values == 0).fillna(False) & ((expected == 0).fillna(False) | expected.isna())] = 0
    try:
        expected[((expected == np.inf) | (expected == -np.inf)).fillna(False)] = fill_value
        original = expected
        expected = expected.astype(s.dtype)
    except ValueError:
        expected = expected.astype(float)
        expected[((expected == np.inf) | (expected == -np.inf)).fillna(False)] = fill_value
        original = expected
        expected = expected.astype(s.dtype)
    expected[mask] = pd.NA
    if not s.dtype.is_unsigned_integer:
        original = pd.Series(original)
        if op_name in ['__rtruediv__', '__rdiv__']:
            mask |= original.isna()
            original = original.fillna(0).astype('int')
        original = original.astype('float')
        original[mask] = np.nan
        tm.assert_series_equal(original, expected.astype('float'))
    tm.assert_series_equal(result, expected)