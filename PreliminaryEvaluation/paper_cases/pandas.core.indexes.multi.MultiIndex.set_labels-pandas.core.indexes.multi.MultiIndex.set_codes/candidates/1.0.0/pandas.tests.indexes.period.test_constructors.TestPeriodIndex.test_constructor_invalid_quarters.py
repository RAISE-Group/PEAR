def test_constructor_invalid_quarters(self):
    msg = 'Quarter must be 1 <= q <= 4'
    with pytest.raises(ValueError, match=msg):
        PeriodIndex(year=range(2000, 2004), quarter=list(range(4)), freq='Q-DEC')