def test_constructor_empty_boolean(self):
    cat = pd.Categorical([], categories=[True, False])
    categories = sorted(cat.categories.tolist())
    assert categories == [False, True]