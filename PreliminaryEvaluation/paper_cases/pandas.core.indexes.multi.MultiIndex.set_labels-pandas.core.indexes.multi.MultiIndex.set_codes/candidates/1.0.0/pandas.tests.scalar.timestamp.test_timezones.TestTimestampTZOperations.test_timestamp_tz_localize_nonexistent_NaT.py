@pytest.mark.parametrize('tz', ['Europe/Warsaw', 'dateutil/Europe/Warsaw'])
def test_timestamp_tz_localize_nonexistent_NaT(self, tz):
    ts = Timestamp('2015-03-29 02:20:00')
    result = ts.tz_localize(tz, nonexistent='NaT')
    assert result is NaT