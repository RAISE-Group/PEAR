def test_union_categorical_same_categories_different_order(self):
    a = pd.Series(Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c']))
    b = pd.Series(Categorical(['a', 'b', 'c'], categories=['b', 'a', 'c']))
    result = pd.concat([a, b], ignore_index=True)
    expected = pd.Series(Categorical(['a', 'b', 'c', 'a', 'b', 'c'], categories=['a', 'b', 'c']))
    tm.assert_series_equal(result, expected)