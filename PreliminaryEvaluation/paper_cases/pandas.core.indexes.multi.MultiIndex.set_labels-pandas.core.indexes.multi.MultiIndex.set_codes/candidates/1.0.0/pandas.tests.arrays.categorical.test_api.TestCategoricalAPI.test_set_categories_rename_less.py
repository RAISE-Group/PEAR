def test_set_categories_rename_less(self):
    cat = Categorical(['A', 'B'])
    result = cat.set_categories(['A'], rename=True)
    expected = Categorical(['A', np.nan])
    tm.assert_categorical_equal(result, expected)