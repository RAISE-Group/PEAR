def test_map(self):
    index = self.create_index()
    if isinstance(index, pd.UInt64Index):
        expected = index.astype('int64')
    else:
        expected = index
    result = index.map(lambda x: x)
    tm.assert_index_equal(result, expected)