def test_comprehensive(self):
    df = DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'c'], 'C': pd.date_range('2016-01-01', freq='d', periods=4), 'E': pd.Series(pd.Categorical(['a', 'b', 'c', 'c'])), 'F': pd.Series(pd.Categorical(['a', 'b', 'c', 'c'], ordered=True)), 'G': [1.1, 2.2, 3.3, 4.4], 'I': [True, False, False, True]}, index=pd.Index(range(4), name='idx'))
    out = df.to_json(orient='table')
    result = pd.read_json(out, orient='table')
    tm.assert_frame_equal(df, result)