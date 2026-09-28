def test_dti_with_timedelta64_data_raises(self):
    data = np.array([0], dtype='m8[ns]')
    msg = 'timedelta64\\[ns\\] cannot be converted to datetime64'
    with pytest.raises(TypeError, match=msg):
        DatetimeIndex(data)
    with pytest.raises(TypeError, match=msg):
        to_datetime(data)
    with pytest.raises(TypeError, match=msg):
        DatetimeIndex(pd.TimedeltaIndex(data))
    with pytest.raises(TypeError, match=msg):
        to_datetime(pd.TimedeltaIndex(data))