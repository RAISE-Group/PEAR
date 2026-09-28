def test_error_with_zero_monthends(self):
    msg = 'Offset <0 \\* MonthEnds> did not increment date'
    with pytest.raises(ValueError, match=msg):
        date_range('1/1/2000', '1/1/2001', freq=MonthEnd(0))