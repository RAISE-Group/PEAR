@pytest.mark.parametrize('freq, td, td64', [('S', timedelta(seconds=1), np.timedelta64(1, 's')), ('min', timedelta(minutes=1), np.timedelta64(1, 'm')), ('H', timedelta(hours=1), np.timedelta64(1, 'h')), ('D', timedelta(days=1), np.timedelta64(1, 'D')), ('W', timedelta(weeks=1), np.timedelta64(1, 'W')), ('M', None, np.timedelta64(1, 'M'))])
def test_addition_subtraction_preserve_frequency(self, freq, td, td64):
    ts = Timestamp('2014-03-05 00:00:00', freq=freq)
    original_freq = ts.freq
    assert (ts + 1 * original_freq).freq == original_freq
    assert (ts - 1 * original_freq).freq == original_freq
    if td is not None:
        assert (ts + td).freq == original_freq
        assert (ts - td).freq == original_freq
    assert (ts + td64).freq == original_freq
    assert (ts - td64).freq == original_freq