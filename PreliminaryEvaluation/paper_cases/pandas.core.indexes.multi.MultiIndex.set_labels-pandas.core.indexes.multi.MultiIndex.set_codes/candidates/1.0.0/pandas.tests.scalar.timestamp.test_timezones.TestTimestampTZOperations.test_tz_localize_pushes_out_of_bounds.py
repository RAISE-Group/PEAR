def test_tz_localize_pushes_out_of_bounds(self):
    pac = Timestamp.min.tz_localize('US/Pacific')
    assert pac.value > Timestamp.min.value
    pac.tz_convert('Asia/Tokyo')
    with pytest.raises(OutOfBoundsDatetime):
        Timestamp.min.tz_localize('Asia/Tokyo')
    tokyo = Timestamp.max.tz_localize('Asia/Tokyo')
    assert tokyo.value < Timestamp.max.value
    tokyo.tz_convert('US/Pacific')
    with pytest.raises(OutOfBoundsDatetime):
        Timestamp.max.tz_localize('US/Pacific')