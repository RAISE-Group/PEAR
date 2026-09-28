def test_date_range_timestamp_equiv_from_datetime_instance(self):
    datetime_instance = datetime(2014, 3, 4)
    timestamp_instance = date_range(datetime_instance, periods=1, freq='D')[0]
    ts = Timestamp(datetime_instance, freq='D')
    assert ts == timestamp_instance