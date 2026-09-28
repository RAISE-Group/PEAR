def test_compare_timedelta64_zerodim(self, box_with_array):
    box = box_with_array
    xbox = box_with_array if box_with_array is not pd.Index else np.ndarray
    tdi = pd.timedelta_range('2H', periods=4)
    other = np.array(tdi.to_numpy()[0])
    tdi = tm.box_expected(tdi, box)
    res = tdi <= other
    expected = np.array([True, False, False, False])
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(res, expected)
    with pytest.raises(TypeError):
        tdi >= np.array(4)