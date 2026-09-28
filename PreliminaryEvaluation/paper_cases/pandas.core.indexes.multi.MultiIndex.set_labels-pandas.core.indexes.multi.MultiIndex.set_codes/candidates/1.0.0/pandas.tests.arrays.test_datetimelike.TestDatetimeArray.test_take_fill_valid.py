def test_take_fill_valid(self, datetime_index, tz_naive_fixture):
    dti = datetime_index.tz_localize(tz_naive_fixture)
    arr = DatetimeArray(dti)
    now = pd.Timestamp.now().tz_localize(dti.tz)
    result = arr.take([-1, 1], allow_fill=True, fill_value=now)
    assert result[0] == now
    with pytest.raises(ValueError):
        arr.take([-1, 1], allow_fill=True, fill_value=now - now)
    with pytest.raises(ValueError):
        arr.take([-1, 1], allow_fill=True, fill_value=pd.Period('2014Q1'))
    tz = None if dti.tz is not None else 'US/Eastern'
    now = pd.Timestamp.now().tz_localize(tz)
    with pytest.raises(TypeError):
        arr.take([-1, 1], allow_fill=True, fill_value=now)
    with pytest.raises(ValueError):
        arr.take([-1, 1], allow_fill=True, fill_value=pd.NaT.value)