def test_non_array_raises(self):
    with pytest.raises(ValueError, match='list'):
        DatetimeArray([1, 2, 3])