def test_compat_replace(self):
    result = date_range(Timestamp('1960-04-01 00:00:00', freq='QS-JAN'), periods=76, freq='QS-JAN')
    assert len(result) == 76