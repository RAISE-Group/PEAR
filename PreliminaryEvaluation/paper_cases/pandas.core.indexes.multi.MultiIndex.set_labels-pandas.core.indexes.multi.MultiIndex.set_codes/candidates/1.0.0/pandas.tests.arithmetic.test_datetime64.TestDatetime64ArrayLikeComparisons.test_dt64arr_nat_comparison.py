def test_dt64arr_nat_comparison(self, tz_naive_fixture, box_with_array):
    tz = tz_naive_fixture
    box = box_with_array
    xbox = box if box is not pd.Index else np.ndarray
    ts = pd.Timestamp.now(tz)
    ser = pd.Series([ts, pd.NaT])
    obj = tm.box_expected(ser, box, transpose=False)
    expected = pd.Series([True, False], dtype=np.bool_)
    expected = tm.box_expected(expected, xbox, transpose=False)
    result = obj == ts
    tm.assert_equal(result, expected)