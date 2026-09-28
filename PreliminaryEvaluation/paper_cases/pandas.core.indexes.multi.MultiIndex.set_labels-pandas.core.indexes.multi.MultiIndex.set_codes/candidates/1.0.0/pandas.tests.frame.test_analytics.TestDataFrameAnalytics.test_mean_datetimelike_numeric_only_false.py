@pytest.mark.xfail(reason='casts to object-dtype and then tries to add timestamps', raises=TypeError, strict=True)
def test_mean_datetimelike_numeric_only_false(self):
    df = pd.DataFrame({'A': np.arange(3), 'B': pd.date_range('2016-01-01', periods=3), 'C': pd.timedelta_range('1D', periods=3), 'D': pd.period_range('2016', periods=3, freq='A')})
    result = df.mean(numeric_only=False)
    expected = pd.Series({'A': 1, 'B': df.loc[1, 'B'], 'C': df.loc[1, 'C'], 'D': df.loc[1, 'D']})
    tm.assert_series_equal(result, expected)