@pytest.mark.parametrize('cache', [True, False])
def test_datetime_bool(self, cache):
    with pytest.raises(TypeError):
        to_datetime(False)
    assert to_datetime(False, errors='coerce', cache=cache) is NaT
    assert to_datetime(False, errors='ignore', cache=cache) is False
    with pytest.raises(TypeError):
        to_datetime(True)
    assert to_datetime(True, errors='coerce', cache=cache) is NaT
    assert to_datetime(True, errors='ignore', cache=cache) is True
    with pytest.raises(TypeError):
        to_datetime([False, datetime.today()], cache=cache)
    with pytest.raises(TypeError):
        to_datetime(['20130101', True], cache=cache)
    tm.assert_index_equal(to_datetime([0, False, NaT, 0.0], errors='coerce', cache=cache), DatetimeIndex([to_datetime(0, cache=cache), NaT, NaT, to_datetime(0, cache=cache)]))