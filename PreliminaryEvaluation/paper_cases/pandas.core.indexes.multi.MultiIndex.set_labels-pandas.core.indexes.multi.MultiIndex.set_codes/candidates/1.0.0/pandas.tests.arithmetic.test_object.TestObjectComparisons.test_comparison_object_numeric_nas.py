def test_comparison_object_numeric_nas(self):
    ser = Series(np.random.randn(10), dtype=object)
    shifted = ser.shift(2)
    ops = ['lt', 'le', 'gt', 'ge', 'eq', 'ne']
    for op in ops:
        func = getattr(operator, op)
        result = func(ser, shifted)
        expected = func(ser.astype(float), shifted.astype(float))
        tm.assert_series_equal(result, expected)