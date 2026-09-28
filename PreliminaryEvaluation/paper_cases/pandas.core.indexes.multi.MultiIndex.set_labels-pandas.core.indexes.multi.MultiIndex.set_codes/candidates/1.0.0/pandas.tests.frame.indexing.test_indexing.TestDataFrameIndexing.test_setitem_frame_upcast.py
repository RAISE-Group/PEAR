def test_setitem_frame_upcast(self):
    df = DataFrame([[1, 2, 'foo'], [3, 4, 'bar']], columns=['A', 'B', 'C'])
    df2 = df.copy()
    df2.loc[:, ['A', 'B']] = df.loc[:, ['A', 'B']] + 0.5
    expected = df.reindex(columns=['A', 'B'])
    expected += 0.5
    expected['C'] = df['C']
    tm.assert_frame_equal(df2, expected)