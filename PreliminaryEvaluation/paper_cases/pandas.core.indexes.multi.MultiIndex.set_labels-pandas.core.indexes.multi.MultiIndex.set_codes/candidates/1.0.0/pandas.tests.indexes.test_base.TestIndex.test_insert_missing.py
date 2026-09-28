def test_insert_missing(self, nulls_fixture):
    expected = Index(['a', nulls_fixture, 'b', 'c'])
    result = Index(list('abc')).insert(1, nulls_fixture)
    tm.assert_index_equal(result, expected)