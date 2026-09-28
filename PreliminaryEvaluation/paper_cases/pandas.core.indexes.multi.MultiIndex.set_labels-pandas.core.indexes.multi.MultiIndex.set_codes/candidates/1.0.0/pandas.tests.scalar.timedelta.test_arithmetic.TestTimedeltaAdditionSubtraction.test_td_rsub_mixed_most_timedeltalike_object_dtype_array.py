def test_td_rsub_mixed_most_timedeltalike_object_dtype_array(self):
    now = Timestamp.now()
    arr = np.array([now, Timedelta('1D'), np.timedelta64(2, 'h')])
    with pytest.raises(TypeError):
        Timedelta('1D') - arr