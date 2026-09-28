def test_positional_take_unobserved(self, ordered_fixture):
    cat = pd.Categorical(['a', 'b'], categories=['a', 'b', 'c'], ordered=ordered_fixture)
    result = cat.take([1, 0], allow_fill=False)
    expected = pd.Categorical(['b', 'a'], categories=cat.categories, ordered=ordered_fixture)
    tm.assert_categorical_equal(result, expected)