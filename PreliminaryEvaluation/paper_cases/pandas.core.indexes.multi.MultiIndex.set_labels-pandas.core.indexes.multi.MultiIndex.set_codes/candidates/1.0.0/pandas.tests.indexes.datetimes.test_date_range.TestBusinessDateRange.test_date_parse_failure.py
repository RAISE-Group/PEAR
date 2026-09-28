def test_date_parse_failure(self):
    badly_formed_date = '2007/100/1'
    with pytest.raises(ValueError):
        Timestamp(badly_formed_date)
    with pytest.raises(ValueError):
        bdate_range(start=badly_formed_date, periods=10)
    with pytest.raises(ValueError):
        bdate_range(end=badly_formed_date, periods=10)
    with pytest.raises(ValueError):
        bdate_range(badly_formed_date, badly_formed_date)