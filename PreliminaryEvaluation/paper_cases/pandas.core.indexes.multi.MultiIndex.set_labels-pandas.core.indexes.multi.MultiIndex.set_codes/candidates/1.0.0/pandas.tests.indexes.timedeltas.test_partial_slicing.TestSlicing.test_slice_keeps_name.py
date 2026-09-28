def test_slice_keeps_name(self):
    dr = pd.timedelta_range('1d', '5d', freq='H', name='timebucket')
    assert dr[1:].name == dr.name