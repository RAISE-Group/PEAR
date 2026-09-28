def test_reindex_single_named_indexer(self):
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [1, 2, 3]})
    result = df.reindex([0, 1], columns=['A'])
    expected = pd.DataFrame({'A': [1, 2]})
    tm.assert_frame_equal(result, expected)