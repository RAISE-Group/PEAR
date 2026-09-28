def test_slicing_directly(self):
    cat = Categorical(['a', 'b', 'c', 'd', 'a', 'b', 'c'])
    sliced = cat[3]
    assert sliced == 'd'
    sliced = cat[3:5]
    expected = Categorical(['d', 'a'], categories=['a', 'b', 'c', 'd'])
    tm.assert_numpy_array_equal(sliced._codes, expected._codes)
    tm.assert_index_equal(sliced.categories, expected.categories)