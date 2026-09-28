def test_td_sub_mixed_most_timedeltalike_object_dtype_array(self):
    now = Timestamp.now()
    arr = np.array([now, Timedelta('1D'), np.timedelta64(2, 'h')])
    exp = np.array([now - Timedelta('1D'), Timedelta('0D'), np.timedelta64(2, 'h') - Timedelta('1D')])
    res = arr - Timedelta('1D')
    tm.assert_numpy_array_equal(res, exp)