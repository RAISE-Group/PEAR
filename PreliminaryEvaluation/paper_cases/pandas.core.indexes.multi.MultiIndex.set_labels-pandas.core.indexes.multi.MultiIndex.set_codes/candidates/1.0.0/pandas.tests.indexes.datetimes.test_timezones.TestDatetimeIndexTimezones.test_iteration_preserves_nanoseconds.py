@pytest.mark.parametrize('tz', [None, 'UTC', 'US/Central', dateutil.tz.tzoffset(None, -28800)])
@pytest.mark.usefixtures('datetime_tz_utc')
def test_iteration_preserves_nanoseconds(self, tz):
    index = DatetimeIndex(['2018-02-08 15:00:00.168456358', '2018-02-08 15:00:00.168456359'], tz=tz)
    for i, ts in enumerate(index):
        assert ts == index[i]