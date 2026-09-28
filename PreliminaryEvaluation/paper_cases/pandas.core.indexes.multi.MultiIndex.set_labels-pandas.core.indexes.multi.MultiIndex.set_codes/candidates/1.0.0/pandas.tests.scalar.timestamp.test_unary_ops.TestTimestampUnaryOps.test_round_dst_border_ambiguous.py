@pytest.mark.parametrize('method', ['ceil', 'round', 'floor'])
def test_round_dst_border_ambiguous(self, method):
    ts = Timestamp('2017-10-29 00:00:00', tz='UTC').tz_convert('Europe/Madrid')
    result = getattr(ts, method)('H', ambiguous=True)
    assert result == ts
    result = getattr(ts, method)('H', ambiguous=False)
    expected = Timestamp('2017-10-29 01:00:00', tz='UTC').tz_convert('Europe/Madrid')
    assert result == expected
    result = getattr(ts, method)('H', ambiguous='NaT')
    assert result is NaT
    with pytest.raises(pytz.AmbiguousTimeError):
        getattr(ts, method)('H', ambiguous='raise')