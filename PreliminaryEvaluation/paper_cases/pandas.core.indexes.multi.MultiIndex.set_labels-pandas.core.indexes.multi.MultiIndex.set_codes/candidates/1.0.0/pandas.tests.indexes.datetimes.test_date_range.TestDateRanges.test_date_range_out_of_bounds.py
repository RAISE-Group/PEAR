def test_date_range_out_of_bounds(self):
    with pytest.raises(OutOfBoundsDatetime):
        date_range('2016-01-01', periods=100000, freq='D')
    with pytest.raises(OutOfBoundsDatetime):
        date_range(end='1763-10-12', periods=100000, freq='D')