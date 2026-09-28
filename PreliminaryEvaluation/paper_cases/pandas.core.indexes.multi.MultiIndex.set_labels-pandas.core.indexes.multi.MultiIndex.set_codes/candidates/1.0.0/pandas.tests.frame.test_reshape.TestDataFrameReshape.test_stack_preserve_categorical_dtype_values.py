def test_stack_preserve_categorical_dtype_values(self):
    cat = pd.Categorical(['a', 'a', 'b', 'c'])
    df = pd.DataFrame({'A': cat, 'B': cat})
    result = df.stack()
    index = pd.MultiIndex.from_product([[0, 1, 2, 3], ['A', 'B']])
    expected = pd.Series(pd.Categorical(['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c']), index=index)
    tm.assert_series_equal(result, expected)