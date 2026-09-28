def test_periods_number_check(self):
    msg = 'Of the three parameters: start, end, and periods, exactly two must be specified'
    with pytest.raises(ValueError, match=msg):
        period_range('2011-1-1', '2012-1-1', 'B')