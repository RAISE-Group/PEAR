def test_exceptions(self):
    with pytest.raises(TypeError, match='Only list-like objects are allowed'):
        safe_sort(values=1)
    with pytest.raises(TypeError, match='Only list-like objects or None'):
        safe_sort(values=[0, 1, 2], codes=1)
    with pytest.raises(ValueError, match='values should be unique'):
        safe_sort(values=[0, 1, 2, 1], codes=[0, 1])