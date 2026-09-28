@pytest.mark.parametrize('first,last,offset,exp_first,exp_last', [('19910905', '19920406', 'D', '19910905', '19920406'), ('19910905 00:00', '19920406 06:00', 'D', '19910905', '19920406'), ('19910905 06:00', '19920406 06:00', 'H', '19910905 06:00', '19920406 06:00'), ('19910906', '19920406', 'M', '1991-09', '1992-04'), ('19910831', '19920430', 'M', '1991-08', '1992-04'), ('1991-08', '1992-04', 'M', '1991-08', '1992-04')])
def test_get_period_range_edges(self, first, last, offset, exp_first, exp_last):
    first = pd.Period(first)
    last = pd.Period(last)
    exp_first = pd.Period(exp_first, freq=offset)
    exp_last = pd.Period(exp_last, freq=offset)
    offset = pd.tseries.frequencies.to_offset(offset)
    result = _get_period_range_edges(first, last, offset)
    expected = (exp_first, exp_last)
    assert result == expected