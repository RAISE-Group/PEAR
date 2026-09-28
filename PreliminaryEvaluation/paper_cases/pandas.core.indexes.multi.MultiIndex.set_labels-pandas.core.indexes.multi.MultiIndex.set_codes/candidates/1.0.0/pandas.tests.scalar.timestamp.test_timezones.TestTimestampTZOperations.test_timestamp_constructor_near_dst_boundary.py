def test_timestamp_constructor_near_dst_boundary(self):
    for tz in ['Europe/Brussels', 'Europe/Prague']:
        result = Timestamp('2015-10-25 01:00', tz=tz)
        expected = Timestamp('2015-10-25 01:00').tz_localize(tz)
        assert result == expected
        with pytest.raises(pytz.AmbiguousTimeError):
            Timestamp('2015-10-25 02:00', tz=tz)
    result = Timestamp('2017-03-26 01:00', tz='Europe/Paris')
    expected = Timestamp('2017-03-26 01:00').tz_localize('Europe/Paris')
    assert result == expected
    with pytest.raises(pytz.NonExistentTimeError):
        Timestamp('2017-03-26 02:00', tz='Europe/Paris')
    naive = Timestamp('2015-11-18 10:00:00')
    result = naive.tz_localize('UTC').tz_convert('Asia/Kolkata')
    expected = Timestamp('2015-11-18 15:30:00+0530', tz='Asia/Kolkata')
    assert result == expected
    result = Timestamp('2017-03-26 00:00', tz='Europe/Paris')
    expected = Timestamp('2017-03-26 00:00:00+0100', tz='Europe/Paris')
    assert result == expected
    result = Timestamp('2017-03-26 01:00', tz='Europe/Paris')
    expected = Timestamp('2017-03-26 01:00:00+0100', tz='Europe/Paris')
    assert result == expected
    with pytest.raises(pytz.NonExistentTimeError):
        Timestamp('2017-03-26 02:00', tz='Europe/Paris')
    result = Timestamp('2017-03-26 02:00:00+0100', tz='Europe/Paris')
    naive = Timestamp(result.value)
    expected = naive.tz_localize('UTC').tz_convert('Europe/Paris')
    assert result == expected
    result = Timestamp('2017-03-26 03:00', tz='Europe/Paris')
    expected = Timestamp('2017-03-26 03:00:00+0200', tz='Europe/Paris')
    assert result == expected