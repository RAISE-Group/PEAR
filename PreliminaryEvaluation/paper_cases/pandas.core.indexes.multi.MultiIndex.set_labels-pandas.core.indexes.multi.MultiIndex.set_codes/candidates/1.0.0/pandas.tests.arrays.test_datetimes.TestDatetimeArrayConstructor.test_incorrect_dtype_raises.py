def test_incorrect_dtype_raises(self):
    with pytest.raises(ValueError, match="Unexpected value for 'dtype'."):
        DatetimeArray(np.array([1, 2, 3], dtype='i8'), dtype='category')