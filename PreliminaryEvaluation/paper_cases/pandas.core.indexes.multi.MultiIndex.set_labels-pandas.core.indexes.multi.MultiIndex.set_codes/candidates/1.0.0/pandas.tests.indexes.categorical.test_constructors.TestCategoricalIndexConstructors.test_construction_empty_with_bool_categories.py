def test_construction_empty_with_bool_categories(self):
    cat = CategoricalIndex([], categories=[True, False])
    categories = sorted(cat.categories.tolist())
    assert categories == [False, True]