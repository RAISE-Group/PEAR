def test_compare_zerodim(self, tz_naive_fixture, box_with_array):
    tz = tz_naive_fixture
    box = box_with_array
    xbox = box_with_array if box_with_array is not pd.Index else np.ndarray
    dti = date_range('20130101', periods=3, tz=tz)
    other = np.array(dti.to_numpy()[0])
    dtarr = tm.box_expected(dti, box)
    result = dtarr <= other
    expected = np.array([True, False, False])
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(result, expected)