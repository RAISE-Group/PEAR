def test_comparison_operators_with_nas(self):
    ser = Series(bdate_range('1/1/2000', periods=10), dtype=object)
    ser[::2] = np.nan
    ops = ['lt', 'le', 'gt', 'ge', 'eq', 'ne']
    for op in ops:
        val = ser[5]
        f = getattr(operator, op)
        result = f(ser, val)
        expected = f(ser.dropna(), val).reindex(ser.index)
        if op == 'ne':
            expected = expected.fillna(True).astype(bool)
        else:
            expected = expected.fillna(False).astype(bool)
        tm.assert_series_equal(result, expected)