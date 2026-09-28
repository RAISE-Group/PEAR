def test_crosstab_with_numpy_size(self):
    df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 6, 'B': ['A', 'B', 'C'] * 8, 'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4, 'D': np.random.randn(24), 'E': np.random.randn(24)})
    result = pd.crosstab(index=[df['A'], df['B']], columns=[df['C']], margins=True, aggfunc=np.size, values=df['D'])
    expected_index = pd.MultiIndex(levels=[['All', 'one', 'three', 'two'], ['', 'A', 'B', 'C']], codes=[[1, 1, 1, 2, 2, 2, 3, 3, 3, 0], [1, 2, 3, 1, 2, 3, 1, 2, 3, 0]], names=['A', 'B'])
    expected_column = pd.Index(['bar', 'foo', 'All'], dtype='object', name='C')
    expected_data = np.array([[2.0, 2.0, 4.0], [2.0, 2.0, 4.0], [2.0, 2.0, 4.0], [2.0, np.nan, 2.0], [np.nan, 2.0, 2.0], [2.0, np.nan, 2.0], [np.nan, 2.0, 2.0], [2.0, np.nan, 2.0], [np.nan, 2.0, 2.0], [12.0, 12.0, 24.0]])
    expected = pd.DataFrame(expected_data, index=expected_index, columns=expected_column)
    tm.assert_frame_equal(result, expected)