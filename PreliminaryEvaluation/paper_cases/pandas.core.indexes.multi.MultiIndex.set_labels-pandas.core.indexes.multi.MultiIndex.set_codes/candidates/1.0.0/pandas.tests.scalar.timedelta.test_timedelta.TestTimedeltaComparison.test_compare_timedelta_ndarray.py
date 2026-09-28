def test_compare_timedelta_ndarray(self):
    periods = [Timedelta('0 days 01:00:00'), Timedelta('0 days 01:00:00')]
    arr = np.array(periods)
    result = arr[0] > arr
    expected = np.array([False, False])
    tm.assert_numpy_array_equal(result, expected)