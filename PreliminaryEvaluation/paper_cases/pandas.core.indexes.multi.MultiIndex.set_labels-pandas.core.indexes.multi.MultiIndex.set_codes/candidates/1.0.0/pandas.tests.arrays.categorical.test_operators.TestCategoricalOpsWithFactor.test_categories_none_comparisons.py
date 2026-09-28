def test_categories_none_comparisons(self):
    factor = Categorical(['a', 'b', 'b', 'a', 'a', 'c', 'c', 'c'], ordered=True)
    tm.assert_categorical_equal(factor, self.factor)