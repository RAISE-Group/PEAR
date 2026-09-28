def test_combine_first(self):
    didx = pd.date_range(start='1950-01-31', end='1950-07-31', freq='M')
    pidx = pd.period_range(start=pd.Period('1950-1'), end=pd.Period('1950-7'), freq='M')
    for idx in [didx, pidx]:
        a = pd.Series([1, np.nan, np.nan, 4, 5, np.nan, 7], index=idx)
        b = pd.Series([9, 9, 9, 9, 9, 9, 9], index=idx)
        result = a.combine_first(b)
        expected = pd.Series([1, 9, 9, 4, 5, 9, 7], index=idx, dtype=np.float64)
        tm.assert_series_equal(result, expected)