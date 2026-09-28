def test_timestamp_constructor_tz_utc(self):
    utc_stamp = Timestamp('3/11/2012 05:00', tz='utc')
    assert utc_stamp.tzinfo is pytz.utc
    assert utc_stamp.hour == 5
    utc_stamp = Timestamp('3/11/2012 05:00').tz_localize('utc')
    assert utc_stamp.hour == 5