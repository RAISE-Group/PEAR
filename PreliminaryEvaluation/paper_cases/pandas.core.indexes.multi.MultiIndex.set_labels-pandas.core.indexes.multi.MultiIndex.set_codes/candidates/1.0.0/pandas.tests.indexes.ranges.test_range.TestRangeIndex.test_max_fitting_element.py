def test_max_fitting_element(self):
    result = RangeIndex(0, 20, 2)._max_fitting_element(17)
    assert 16 == result
    result = RangeIndex(1, 6)._max_fitting_element(4)
    assert 4 == result
    result = RangeIndex(18, -2, -2)._max_fitting_element(17)
    assert 16 == result
    result = RangeIndex(5, 0, -1)._max_fitting_element(4)
    assert 4 == result
    big_num = 500000000000000000000000
    result = RangeIndex(5, big_num * 2, 1)._max_fitting_element(big_num)
    assert big_num == result