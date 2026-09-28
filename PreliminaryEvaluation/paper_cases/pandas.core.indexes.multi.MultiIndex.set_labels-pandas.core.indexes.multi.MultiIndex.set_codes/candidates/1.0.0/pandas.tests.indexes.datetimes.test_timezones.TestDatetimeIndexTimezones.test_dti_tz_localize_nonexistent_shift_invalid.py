@pytest.mark.parametrize('offset', [-1, 1])
@pytest.mark.parametrize('tz_type', ['', 'dateutil/'])
def test_dti_tz_localize_nonexistent_shift_invalid(self, offset, tz_type):
    tz = tz_type + 'Europe/Warsaw'
    dti = DatetimeIndex([Timestamp('2015-03-29 02:20:00')])
    msg = 'The provided timedelta will relocalize on a nonexistent time'
    with pytest.raises(ValueError, match=msg):
        dti.tz_localize(tz, nonexistent=timedelta(seconds=offset))