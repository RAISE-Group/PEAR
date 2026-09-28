def test_contains_method_removed(self, indices):
    if isinstance(indices, pd.IntervalIndex):
        indices.contains(1)
    else:
        with pytest.raises(AttributeError):
            indices.contains(1)