def test_cached_properties_not_settable(self):
    index = pd.Index([1, 2, 3])
    with pytest.raises(AttributeError, match="Can't set attribute"):
        index.is_unique = False