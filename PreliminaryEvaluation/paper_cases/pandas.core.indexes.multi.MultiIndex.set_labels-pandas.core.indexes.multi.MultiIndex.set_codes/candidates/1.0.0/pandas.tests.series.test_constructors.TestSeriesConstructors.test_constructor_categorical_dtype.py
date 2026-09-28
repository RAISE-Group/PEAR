def test_constructor_categorical_dtype(self):
    result = pd.Series(['a', 'b'], dtype=CategoricalDtype(['a', 'b', 'c'], ordered=True))
    assert is_categorical_dtype(result) is True
    tm.assert_index_equal(result.cat.categories, pd.Index(['a', 'b', 'c']))
    assert result.cat.ordered
    result = pd.Series(['a', 'b'], dtype=CategoricalDtype(['b', 'a']))
    assert is_categorical_dtype(result)
    tm.assert_index_equal(result.cat.categories, pd.Index(['b', 'a']))
    assert result.cat.ordered is False
    result = Series('a', index=[0, 1], dtype=CategoricalDtype(['a', 'b'], ordered=True))
    expected = Series(['a', 'a'], index=[0, 1], dtype=CategoricalDtype(['a', 'b'], ordered=True))
    tm.assert_series_equal(result, expected, check_categorical=True)