def test_from_sequence_dtype(self):
    msg = 'dtype .*object.* cannot be converted to timedelta64'
    with pytest.raises(ValueError, match=msg):
        TimedeltaArray._from_sequence([], dtype=object)