def test_from_inferred_categories_coerces(self):
    cats = ['1', '2', 'bad']
    codes = np.array([0, 0, 1, 2], dtype='i8')
    dtype = CategoricalDtype([1, 2])
    result = Categorical._from_inferred_categories(cats, codes, dtype)
    expected = Categorical([1, 1, 2, np.nan])
    tm.assert_categorical_equal(result, expected)