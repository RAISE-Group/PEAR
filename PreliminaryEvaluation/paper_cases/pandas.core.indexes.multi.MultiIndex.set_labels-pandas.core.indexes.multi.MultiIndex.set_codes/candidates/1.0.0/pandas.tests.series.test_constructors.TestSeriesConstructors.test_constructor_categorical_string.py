def test_constructor_categorical_string(self):
    cdt = CategoricalDtype(categories=list('dabc'), ordered=True)
    expected = Series(list('abcabc'), dtype=cdt)
    cat = Categorical(list('abcabc'), dtype=cdt)
    result = Series(cat, dtype='category')
    tm.assert_series_equal(result, expected)
    result = Series(result, dtype='category')
    tm.assert_series_equal(result, expected)