@pytest.mark.parametrize('tz', [None, pytz.timezone('US/Pacific')])
def test_disallow_setting_tz(self, tz):
    ts = Timestamp('2010')
    with pytest.raises(AttributeError):
        ts.tz = tz