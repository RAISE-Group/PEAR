def _check(self, values, func, expected):
    idx = pd.PeriodIndex(values)
    result = func(idx)
    assert isinstance(expected, (pd.Index, np.ndarray))
    tm.assert_equal(result, expected)
    s = pd.Series(values)
    result = func(s)
    exp = pd.Series(expected, name=values.name)
    tm.assert_series_equal(result, exp)