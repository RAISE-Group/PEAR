def test_non_unique_invalid(self):
    with pytest.raises(ValueError):
        CategoricalDtype([1, 2, 1])