def test_categorical_categories(self):
    c1 = CategoricalDtype(Categorical(['a', 'b']))
    tm.assert_index_equal(c1.categories, pd.Index(['a', 'b']))
    c1 = CategoricalDtype(CategoricalIndex(['a', 'b']))
    tm.assert_index_equal(c1.categories, pd.Index(['a', 'b']))