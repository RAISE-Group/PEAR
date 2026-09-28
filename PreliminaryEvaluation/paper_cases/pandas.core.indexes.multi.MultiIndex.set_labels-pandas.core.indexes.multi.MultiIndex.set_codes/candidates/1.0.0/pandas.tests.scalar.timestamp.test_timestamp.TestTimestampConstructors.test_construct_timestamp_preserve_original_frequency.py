def test_construct_timestamp_preserve_original_frequency(self):
    result = Timestamp(Timestamp('2010-08-08', freq='D')).freq
    expected = offsets.Day()
    assert result == expected