@pytest.mark.parametrize('dt', [np.datetime64('1000-01-01'), np.datetime64('5000-01-02')])
@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_dt64s_out_of_bounds(self, cache, dt):
    msg = 'Out of bounds nanosecond timestamp: {}'.format(dt)
    with pytest.raises(OutOfBoundsDatetime, match=msg):
        pd.to_datetime(dt, errors='raise')
    with pytest.raises(OutOfBoundsDatetime, match=msg):
        Timestamp(dt)
    assert pd.to_datetime(dt, errors='coerce', cache=cache) is NaT