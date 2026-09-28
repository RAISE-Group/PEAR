def test_to_timestamp_out_of_bounds(self):
    per = Period('0001-01-01', freq='B')
    with pytest.raises(OutOfBoundsDatetime):
        per.to_timestamp()