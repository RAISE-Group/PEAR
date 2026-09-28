@pytest.mark.parametrize('freq, error_msg', [('Y', '<YearEnd: month=12> is a non-fixed frequency'), ('M', '<MonthEnd> is a non-fixed frequency'), ('foobar', 'Invalid frequency: foobar')])
def test_round_invalid(self, freq, error_msg):
    dti = date_range('20130101 09:10:11', periods=5)
    dti = dti.tz_localize('UTC').tz_convert('US/Eastern')
    with pytest.raises(ValueError, match=error_msg):
        dti.round(freq)