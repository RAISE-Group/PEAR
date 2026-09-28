def test_construction_with_tz_and_tz_aware_dti(self):
    dti = date_range('2016-01-01', periods=3, tz='US/Central')
    with pytest.raises(TypeError):
        DatetimeIndex(dti, tz='Asia/Tokyo')