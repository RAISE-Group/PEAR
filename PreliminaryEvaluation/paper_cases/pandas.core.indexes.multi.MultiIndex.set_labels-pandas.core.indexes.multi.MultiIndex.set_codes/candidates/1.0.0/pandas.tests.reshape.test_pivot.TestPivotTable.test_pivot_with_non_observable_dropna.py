def test_pivot_with_non_observable_dropna(self, dropna):
    df = pd.DataFrame({'A': pd.Categorical([np.nan, 'low', 'high', 'low', 'high'], categories=['low', 'high'], ordered=True), 'B': range(5)})
    result = df.pivot_table(index='A', values='B', dropna=dropna)
    expected = pd.DataFrame({'B': [2, 3]}, index=pd.Index(pd.Categorical.from_codes([0, 1], categories=['low', 'high'], ordered=True), name='A'))
    tm.assert_frame_equal(result, expected)
    df = pd.DataFrame({'A': pd.Categorical(['left', 'low', 'high', 'low', 'high'], categories=['low', 'high', 'left'], ordered=True), 'B': range(5)})
    result = df.pivot_table(index='A', values='B', dropna=dropna)
    expected = pd.DataFrame({'B': [2, 3, 0]}, index=pd.Index(pd.Categorical.from_codes([0, 1, 2], categories=['low', 'high', 'left'], ordered=True), name='A'))
    tm.assert_frame_equal(result, expected)