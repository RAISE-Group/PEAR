def test_tuple_categories(self):
    categories = [(1, 'a'), (2, 'b'), (3, 'c')]
    result = CategoricalDtype(categories)
    assert all(result.categories == categories)