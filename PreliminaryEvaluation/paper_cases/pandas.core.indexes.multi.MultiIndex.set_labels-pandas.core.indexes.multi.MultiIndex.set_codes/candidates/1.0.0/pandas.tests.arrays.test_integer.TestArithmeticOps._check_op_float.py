def _check_op_float(self, result, expected, mask, s, op_name, other):
    expected[mask] = np.nan
    if 'floordiv' in op_name:
        mask2 = np.isinf(expected) & np.isnan(result)
        expected[mask2] = np.nan
    tm.assert_series_equal(result, expected)