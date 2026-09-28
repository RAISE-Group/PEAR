def test_construct_from_string_raises(self):
    with pytest.raises(TypeError, match='notatz'):
        DatetimeTZDtype.construct_from_string('datetime64[ns, notatz]')
    msg = "^Cannot construct a 'DatetimeTZDtype'"
    with pytest.raises(TypeError, match=msg):
        DatetimeTZDtype.construct_from_string(['datetime64[ns, notatz]'])
    with pytest.raises(TypeError, match=msg):
        DatetimeTZDtype.construct_from_string('datetime64[ps, UTC]')
    with pytest.raises(TypeError, match=msg):
        DatetimeTZDtype.construct_from_string('datetime64[ns, dateutil/invalid]')