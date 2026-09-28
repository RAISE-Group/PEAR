def test_date_range_timestamp_equiv_preserve_frequency(self):
    timestamp_instance = date_range('2014-03-05', periods=1, freq='D')[0]
    ts = Timestamp('2014-03-05', freq='D')
    assert timestamp_instance == ts