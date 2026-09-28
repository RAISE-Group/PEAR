def test_freq_conversion(self):
    td = Timedelta('1 days 2 hours 3 ns')
    result = td / np.timedelta64(1, 'D')
    assert result == td.value / float(86400 * 1000000000.0)
    result = td / np.timedelta64(1, 's')
    assert result == td.value / float(1000000000.0)
    result = td / np.timedelta64(1, 'ns')
    assert result == td.value
    td = Timedelta('1 days 2 hours 3 ns')
    result = td // np.timedelta64(1, 'D')
    assert result == 1
    result = td // np.timedelta64(1, 's')
    assert result == 93600
    result = td // np.timedelta64(1, 'ns')
    assert result == td.value