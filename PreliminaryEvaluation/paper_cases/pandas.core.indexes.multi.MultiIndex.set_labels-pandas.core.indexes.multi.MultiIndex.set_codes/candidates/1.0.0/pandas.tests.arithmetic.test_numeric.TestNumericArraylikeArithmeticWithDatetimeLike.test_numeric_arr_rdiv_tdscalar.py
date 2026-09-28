def test_numeric_arr_rdiv_tdscalar(self, three_days, numeric_idx, box):
    index = numeric_idx[1:3]
    expected = TimedeltaIndex(['3 Days', '36 Hours'])
    index = tm.box_expected(index, box)
    expected = tm.box_expected(expected, box)
    result = three_days / index
    tm.assert_equal(result, expected)
    with pytest.raises(TypeError):
        index / three_days