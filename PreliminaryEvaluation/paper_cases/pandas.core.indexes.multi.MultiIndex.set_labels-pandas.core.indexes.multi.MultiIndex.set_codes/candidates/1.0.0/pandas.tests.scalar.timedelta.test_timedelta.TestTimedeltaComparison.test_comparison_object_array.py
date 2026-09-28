def test_comparison_object_array(self):
    td = Timedelta('2 days')
    other = Timedelta('3 hours')
    arr = np.array([other, td], dtype=object)
    res = arr == td
    expected = np.array([False, True], dtype=bool)
    assert (res == expected).all()
    arr = np.array([[other, td], [td, other]], dtype=object)
    res = arr != td
    expected = np.array([[True, False], [False, True]], dtype=bool)
    assert res.shape == expected.shape
    assert (res == expected).all()