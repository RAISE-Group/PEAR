def test_freq_infer_raises(self):
    with pytest.raises(ValueError, match='Frequency inference'):
        DatetimeArray(np.array([1, 2, 3], dtype='i8'), freq='infer')