def test_full_format_converters(self):

    def conv(v):
        return v.astype('m8[ns]')
    d1 = np.timedelta64(1, 'D')
    assert Timedelta('1days') == conv(d1)
    assert Timedelta('1days,') == conv(d1)
    assert Timedelta('- 1days,') == -conv(d1)
    assert Timedelta('00:00:01') == conv(np.timedelta64(1, 's'))
    assert Timedelta('06:00:01') == conv(np.timedelta64(6 * 3600 + 1, 's'))
    assert Timedelta('06:00:01.0') == conv(np.timedelta64(6 * 3600 + 1, 's'))
    assert Timedelta('06:00:01.01') == conv(np.timedelta64(1000 * (6 * 3600 + 1) + 10, 'ms'))
    assert Timedelta('- 1days, 00:00:01') == conv(-d1 + np.timedelta64(1, 's'))
    assert Timedelta('1days, 06:00:01') == conv(d1 + np.timedelta64(6 * 3600 + 1, 's'))
    assert Timedelta('1days, 06:00:01.01') == conv(d1 + np.timedelta64(1000 * (6 * 3600 + 1) + 10, 'ms'))
    with pytest.raises(ValueError):
        Timedelta('- 1days, 00')