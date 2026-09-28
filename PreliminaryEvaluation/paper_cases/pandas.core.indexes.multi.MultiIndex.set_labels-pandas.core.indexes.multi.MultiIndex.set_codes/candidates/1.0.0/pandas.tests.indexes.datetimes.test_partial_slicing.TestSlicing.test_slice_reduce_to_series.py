def test_slice_reduce_to_series(self):
    df = pd.DataFrame({'A': range(24)}, index=pd.date_range('2000', periods=24, freq='M'))
    expected = pd.Series(range(12), index=pd.date_range('2000', periods=12, freq='M'), name='A')
    result = df.loc['2000', 'A']
    tm.assert_series_equal(result, expected)