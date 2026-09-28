def test_drop_by_numeric_label_loc(self):
    index = Index([1, 2, 3])
    dropped = index.drop(1)
    expected = Index([2, 3])
    tm.assert_index_equal(dropped, expected)