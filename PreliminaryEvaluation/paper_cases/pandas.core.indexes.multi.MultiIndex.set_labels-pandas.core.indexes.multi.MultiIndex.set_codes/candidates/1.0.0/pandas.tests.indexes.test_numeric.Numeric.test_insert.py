def test_insert(self, nulls_fixture):
    index = self.create_index()
    expected = Float64Index([index[0], np.nan] + list(index[1:]))
    result = index.insert(1, nulls_fixture)
    tm.assert_index_equal(result, expected)