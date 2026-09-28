def test_pivot_table_empty_aggfunc(self):
    df = pd.DataFrame({'A': [2, 2, 3, 3, 2], 'id': [5, 6, 7, 8, 9], 'C': ['p', 'q', 'q', 'p', 'q'], 'D': [None, None, None, None, None]})
    result = df.pivot_table(index='A', columns='D', values='id', aggfunc=np.size)
    expected = pd.DataFrame()
    tm.assert_frame_equal(result, expected)