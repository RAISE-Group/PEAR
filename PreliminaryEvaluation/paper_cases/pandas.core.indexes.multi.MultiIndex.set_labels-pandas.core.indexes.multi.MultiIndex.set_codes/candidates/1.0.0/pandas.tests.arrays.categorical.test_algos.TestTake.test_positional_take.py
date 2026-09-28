def test_positional_take(self, ordered_fixture):
    cat = pd.Categorical(['a', 'a', 'b', 'b'], categories=['b', 'a'], ordered=ordered_fixture)
    result = cat.take([0, 1, 2], allow_fill=False)
    expected = pd.Categorical(['a', 'a', 'b'], categories=cat.categories, ordered=ordered_fixture)
    tm.assert_categorical_equal(result, expected)