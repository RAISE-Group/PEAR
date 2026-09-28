@pytest.mark.parametrize('start, index_freq, periods', [('2018-01-01', '12H', 25), ('2018-01-01 0:0:0.124999', '1ns', 1000)])
@pytest.mark.parametrize('round_freq', ['2ns', '3ns', '4ns', '5ns', '6ns', '7ns', '250ns', '500ns', '750ns', '1us', '19us', '250us', '500us', '750us', '1s', '2s', '3s', '12H', '1D'])
def test_round_int64(self, start, index_freq, periods, round_freq):
    dt = date_range(start=start, freq=index_freq, periods=periods)
    unit = to_offset(round_freq).nanos
    result = dt.floor(round_freq)
    diff = dt.asi8 - result.asi8
    mod = result.asi8 % unit
    assert (mod == 0).all(), 'floor not a {} multiple'.format(round_freq)
    assert (0 <= diff).all() and (diff < unit).all(), 'floor error'
    result = dt.ceil(round_freq)
    diff = result.asi8 - dt.asi8
    mod = result.asi8 % unit
    assert (mod == 0).all(), 'ceil not a {} multiple'.format(round_freq)
    assert (0 <= diff).all() and (diff < unit).all(), 'ceil error'
    result = dt.round(round_freq)
    diff = abs(result.asi8 - dt.asi8)
    mod = result.asi8 % unit
    assert (mod == 0).all(), 'round not a {} multiple'.format(round_freq)
    assert (diff <= unit // 2).all(), 'round error'
    if unit % 2 == 0:
        assert (result.asi8[diff == unit // 2] % 2 == 0).all(), 'round half to even error'