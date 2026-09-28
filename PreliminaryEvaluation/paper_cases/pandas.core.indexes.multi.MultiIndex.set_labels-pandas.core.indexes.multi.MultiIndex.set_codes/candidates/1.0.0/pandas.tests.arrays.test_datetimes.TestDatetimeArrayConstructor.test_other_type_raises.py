def test_other_type_raises(self):
    with pytest.raises(ValueError, match="The dtype of 'values' is incorrect.*bool"):
        DatetimeArray(np.array([1, 2, 3], dtype='bool'))