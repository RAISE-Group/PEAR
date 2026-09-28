def test_constructor_empty(self):
    c = Categorical([])
    expected = Index([])
    tm.assert_index_equal(c.categories, expected)
    c = Categorical([], categories=[1, 2, 3])
    expected = pd.Int64Index([1, 2, 3])
    tm.assert_index_equal(c.categories, expected)