def test_slice_keeps_name(self):
    st = pd.Timestamp('2013-07-01 00:00:00', tz='America/Los_Angeles')
    et = pd.Timestamp('2013-07-02 00:00:00', tz='America/Los_Angeles')
    dr = pd.date_range(st, et, freq='H', name='timebucket')
    assert dr[1:].name == dr.name