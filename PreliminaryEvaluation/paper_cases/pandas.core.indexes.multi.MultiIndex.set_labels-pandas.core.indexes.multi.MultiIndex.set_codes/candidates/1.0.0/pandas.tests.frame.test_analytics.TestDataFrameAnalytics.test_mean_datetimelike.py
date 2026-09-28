def test_mean_datetimelike(self):
    df = pd.DataFrame({'A': np.arange(3), 'B': pd.date_range('2016-01-01', periods=3), 'C': pd.timedelta_range('1D', periods=3), 'D': pd.period_range('2016', periods=3, freq='A')})
    result = df.mean(numeric_only=True)
    expected = pd.Series({'A': 1.0})
    tm.assert_series_equal(result, expected)
    result = df.mean()
    expected = pd.Series({'A': 1.0, 'C': df.loc[1, 'C']})
    tm.assert_series_equal(result, expected)