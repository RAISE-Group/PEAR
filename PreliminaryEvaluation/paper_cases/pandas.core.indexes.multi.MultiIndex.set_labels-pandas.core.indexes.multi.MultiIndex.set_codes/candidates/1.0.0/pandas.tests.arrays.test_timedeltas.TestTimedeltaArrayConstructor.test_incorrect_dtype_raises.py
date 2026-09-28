def test_incorrect_dtype_raises(self):
    with pytest.raises(ValueError, match='category cannot be converted to timedelta64\\[ns\\]'):
        TimedeltaArray(np.array([1, 2, 3], dtype='i8'), dtype='category')
    with pytest.raises(ValueError, match='dtype int64 cannot be converted to timedelta64\\[ns\\]'):
        TimedeltaArray(np.array([1, 2, 3], dtype='i8'), dtype=np.dtype('int64'))