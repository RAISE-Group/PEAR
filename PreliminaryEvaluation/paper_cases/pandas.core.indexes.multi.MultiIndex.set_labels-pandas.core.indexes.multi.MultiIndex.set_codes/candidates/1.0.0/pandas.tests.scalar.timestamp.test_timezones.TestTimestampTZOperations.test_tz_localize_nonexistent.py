@pytest.mark.parametrize('stamp, tz', [('2015-03-08 02:00', 'US/Eastern'), ('2015-03-08 02:30', 'US/Pacific'), ('2015-03-29 02:00', 'Europe/Paris'), ('2015-03-29 02:30', 'Europe/Belgrade')])
def test_tz_localize_nonexistent(self, stamp, tz):
    ts = Timestamp(stamp)
    with pytest.raises(NonExistentTimeError):
        ts.tz_localize(tz)
    with pytest.raises(NonExistentTimeError):
        ts.tz_localize(tz, nonexistent='raise')
    assert ts.tz_localize(tz, nonexistent='NaT') is NaT