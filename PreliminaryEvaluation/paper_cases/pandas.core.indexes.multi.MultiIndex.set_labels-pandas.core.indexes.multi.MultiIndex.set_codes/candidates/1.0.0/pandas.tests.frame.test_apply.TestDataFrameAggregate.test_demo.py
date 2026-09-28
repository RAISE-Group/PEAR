def test_demo(self):
    df = pd.DataFrame({'A': range(5), 'B': 5})
    result = df.agg(['min', 'max'])
    expected = DataFrame({'A': [0, 4], 'B': [5, 5]}, columns=['A', 'B'], index=['min', 'max'])
    tm.assert_frame_equal(result, expected)
    result = df.agg({'A': ['min', 'max'], 'B': ['sum', 'max']})
    expected = DataFrame({'A': [4.0, 0.0, np.nan], 'B': [5.0, np.nan, 25.0]}, columns=['A', 'B'], index=['max', 'min', 'sum'])
    tm.assert_frame_equal(result.reindex_like(expected), expected)