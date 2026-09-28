def test_agg_relabel_non_identifier(self):
    df = pd.DataFrame({'group': ['a', 'a', 'b', 'b'], 'A': [0, 1, 2, 3], 'B': [5, 6, 7, 8]})
    result = df.groupby('group').agg(**{'my col': ('A', 'max')})
    expected = pd.DataFrame({'my col': [1, 3]}, index=pd.Index(['a', 'b'], name='group'))
    tm.assert_frame_equal(result, expected)