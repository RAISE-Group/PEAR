def test_disallow_setting_tz(self):
    dti = DatetimeIndex(['2010'], tz='UTC')
    with pytest.raises(AttributeError):
        dti.tz = pytz.timezone('US/Pacific')