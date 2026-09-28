def test_td_floordiv_numeric_scalar(self):
    td = Timedelta(hours=3, minutes=4)
    expected = Timedelta(hours=1, minutes=32)
    assert td // 2 == expected
    assert td // 2.0 == expected
    assert td // np.float64(2.0) == expected
    assert td // np.int32(2.0) == expected
    assert td // np.uint8(2.0) == expected