def test_td64arr_div_int(self, box_with_array):
    idx = TimedeltaIndex(np.arange(5, dtype='int64'))
    idx = tm.box_expected(idx, box_with_array)
    result = idx / 1
    tm.assert_equal(result, idx)
    with pytest.raises(TypeError, match='Cannot divide'):
        1 / idx