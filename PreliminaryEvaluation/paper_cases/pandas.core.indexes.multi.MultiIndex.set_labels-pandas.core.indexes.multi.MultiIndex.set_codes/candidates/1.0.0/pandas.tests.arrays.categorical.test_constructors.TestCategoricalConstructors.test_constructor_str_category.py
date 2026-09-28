@pytest.mark.parametrize('categories', [None, ['a', 'b'], ['a', 'c']])
@pytest.mark.parametrize('ordered', [True, False])
def test_constructor_str_category(self, categories, ordered):
    result = Categorical(['a', 'b'], categories=categories, ordered=ordered, dtype='category')
    expected = Categorical(['a', 'b'], categories=categories, ordered=ordered)
    tm.assert_categorical_equal(result, expected)