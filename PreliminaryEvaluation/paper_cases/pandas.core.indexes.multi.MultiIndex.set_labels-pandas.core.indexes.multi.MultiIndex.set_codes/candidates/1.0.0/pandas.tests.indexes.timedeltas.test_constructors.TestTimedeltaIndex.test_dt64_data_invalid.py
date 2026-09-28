def test_dt64_data_invalid(self):
    dti = pd.date_range('2016-01-01', periods=3)
    msg = 'cannot be converted to timedelta64'
    with pytest.raises(TypeError, match=msg):
        TimedeltaIndex(dti.tz_localize('Europe/Brussels'))
    with pytest.raises(TypeError, match=msg):
        TimedeltaIndex(dti)
    with pytest.raises(TypeError, match=msg):
        TimedeltaIndex(np.asarray(dti))