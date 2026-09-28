@pytest.mark.parametrize('timestamp', ['2018-01-01 0:0:0.124999360', '2018-01-01 0:0:0.125000367', '2018-01-01 0:0:0.125500', '2018-01-01 0:0:0.126500', '2018-01-01 12:00:00', '2019-01-01 12:00:00'])
@pytest.mark.parametrize('freq', ['2ns', '3ns', '4ns', '5ns', '6ns', '7ns', '250ns', '500ns', '750ns', '1us', '19us', '250us', '500us', '750us', '1s', '2s', '3s', '1D'])
def test_round_int64(self, timestamp, freq):
    """check that all rounding modes are accurate to int64 precision
           see GH#22591
        """
    dt = Timestamp(timestamp)
    unit = to_offset(freq).nanos
    result = dt.floor(freq)
    assert result.value % unit == 0, 'floor not a {} multiple'.format(freq)
    assert 0 <= dt.value - result.value < unit, 'floor error'
    result = dt.ceil(freq)
    assert result.value % unit == 0, 'ceil not a {} multiple'.format(freq)
    assert 0 <= result.value - dt.value < unit, 'ceil error'
    result = dt.round(freq)
    assert result.value % unit == 0, 'round not a {} multiple'.format(freq)
    assert abs(result.value - dt.value) <= unit // 2, 'round error'
    if unit % 2 == 0 and abs(result.value - dt.value) == unit // 2:
        assert result.value // unit % 2 == 0, 'round half to even error'