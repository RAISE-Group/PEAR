@pytest.mark.parametrize('categories', [list('abc'), None])
@pytest.mark.parametrize('other', ['category', 'not a category'])
def test_categorical_equality_strings(self, categories, ordered_fixture, other):
    c1 = CategoricalDtype(categories, ordered_fixture)
    result = c1 == other
    expected = other == 'category'
    assert result is expected