@pytest.mark.parametrize('td_scalar', [timedelta(days=1), Timedelta(days=1), Timedelta(days=1).to_timedelta64()])
def test_compare_timedeltalike_scalar(self, box_with_array, td_scalar):
    box = box_with_array
    xbox = box if box is not pd.Index else np.ndarray
    ser = pd.Series([timedelta(days=1), timedelta(days=2)])
    ser = tm.box_expected(ser, box)
    actual = ser > td_scalar
    expected = pd.Series([False, True])
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(actual, expected)