def test_drop_duplicates(self):
    idx = CategoricalIndex([0, 0, 0], name='foo')
    expected = CategoricalIndex([0], name='foo')
    tm.assert_index_equal(idx.drop_duplicates(), expected)
    tm.assert_index_equal(idx.unique(), expected)