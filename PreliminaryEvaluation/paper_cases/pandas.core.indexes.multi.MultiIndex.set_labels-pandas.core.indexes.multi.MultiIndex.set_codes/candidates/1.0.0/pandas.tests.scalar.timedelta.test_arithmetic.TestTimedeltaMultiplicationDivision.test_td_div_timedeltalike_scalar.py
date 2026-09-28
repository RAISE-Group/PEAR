def test_td_div_timedeltalike_scalar(self):
    td = Timedelta(10, unit='d')
    result = td / offsets.Hour(1)
    assert result == 240
    assert td / td == 1
    assert td / np.timedelta64(60, 'h') == 4
    assert np.isnan(td / NaT)