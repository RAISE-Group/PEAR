def test_set_categories_inplace(self):
    cat = self.factor.copy()
    cat.set_categories(['a', 'b', 'c', 'd'], inplace=True)
    tm.assert_index_equal(cat.categories, Index(['a', 'b', 'c', 'd']))