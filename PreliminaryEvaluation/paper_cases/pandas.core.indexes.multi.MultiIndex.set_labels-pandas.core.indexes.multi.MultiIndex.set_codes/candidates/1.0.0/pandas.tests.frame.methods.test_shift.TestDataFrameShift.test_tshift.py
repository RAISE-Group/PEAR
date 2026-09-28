def test_tshift(self, datetime_frame):
    ps = tm.makePeriodFrame()
    shifted = ps.tshift(1)
    unshifted = shifted.tshift(-1)
    tm.assert_frame_equal(unshifted, ps)
    shifted2 = ps.tshift(freq='B')
    tm.assert_frame_equal(shifted, shifted2)
    shifted3 = ps.tshift(freq=offsets.BDay())
    tm.assert_frame_equal(shifted, shifted3)
    with pytest.raises(ValueError, match='does not match'):
        ps.tshift(freq='M')
    shifted = datetime_frame.tshift(1)
    unshifted = shifted.tshift(-1)
    tm.assert_frame_equal(datetime_frame, unshifted)
    shifted2 = datetime_frame.tshift(freq=datetime_frame.index.freq)
    tm.assert_frame_equal(shifted, shifted2)
    inferred_ts = DataFrame(datetime_frame.values, Index(np.asarray(datetime_frame.index)), columns=datetime_frame.columns)
    shifted = inferred_ts.tshift(1)
    unshifted = shifted.tshift(-1)
    tm.assert_frame_equal(shifted, datetime_frame.tshift(1))
    tm.assert_frame_equal(unshifted, inferred_ts)
    no_freq = datetime_frame.iloc[[0, 5, 7], :]
    msg = 'Freq was not given and was not set in the index'
    with pytest.raises(ValueError, match=msg):
        no_freq.tshift()