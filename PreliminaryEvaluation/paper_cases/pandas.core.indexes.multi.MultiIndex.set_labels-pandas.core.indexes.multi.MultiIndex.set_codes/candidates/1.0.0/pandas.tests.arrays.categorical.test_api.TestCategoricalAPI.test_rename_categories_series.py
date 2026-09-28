def test_rename_categories_series(self):
    c = Categorical(['a', 'b'])
    result = c.rename_categories(Series([0, 1], index=['a', 'b']))
    expected = Categorical([0, 1])
    tm.assert_categorical_equal(result, expected)