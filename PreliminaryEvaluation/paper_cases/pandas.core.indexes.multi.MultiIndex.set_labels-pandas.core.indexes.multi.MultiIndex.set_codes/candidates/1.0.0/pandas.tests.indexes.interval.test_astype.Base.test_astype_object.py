def test_astype_object(self, index):
    result = index.astype(object)
    expected = Index(index.values, dtype='object')
    tm.assert_index_equal(result, expected)
    assert not result.equals(index)