def _check(self, values, func, expected):
    idx = pd.PeriodIndex(values)
    result = func(idx)
    tm.assert_equal(result, expected)
    ser = pd.Series(values)
    result = func(ser)
    exp = pd.Series(expected, name=values.name)
    tm.assert_series_equal(result, exp)