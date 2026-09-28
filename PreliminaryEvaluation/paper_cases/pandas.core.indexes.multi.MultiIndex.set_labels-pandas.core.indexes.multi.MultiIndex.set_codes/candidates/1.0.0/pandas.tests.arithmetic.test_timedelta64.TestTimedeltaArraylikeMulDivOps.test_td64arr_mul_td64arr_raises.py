def test_td64arr_mul_td64arr_raises(self, box_with_array):
    idx = TimedeltaIndex(np.arange(5, dtype='int64'))
    idx = tm.box_expected(idx, box_with_array)
    with pytest.raises(TypeError):
        idx * idx