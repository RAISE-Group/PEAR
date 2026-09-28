def test_to_timedelta_float(self):
    arr = np.arange(0, 1, 1e-06)[-10:]
    result = pd.to_timedelta(arr, unit='s')
    expected_asi8 = np.arange(999990000, int(1000000000.0), 1000, dtype='int64')
    tm.assert_numpy_array_equal(result.asi8, expected_asi8)