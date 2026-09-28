def test_pivot_table_aggfunc_scalar_dropna(self, dropna):
    df = pd.DataFrame({'A': ['one', 'two', 'one'], 'x': [3, np.nan, 2], 'y': [1, np.nan, np.nan]})
    result = pd.pivot_table(df, columns='A', aggfunc=np.mean, dropna=dropna)
    data = [[2.5, np.nan], [1, np.nan]]
    col = pd.Index(['one', 'two'], name='A')
    expected = pd.DataFrame(data, index=['x', 'y'], columns=col)
    if dropna:
        expected = expected.dropna(axis='columns')
    tm.assert_frame_equal(result, expected)