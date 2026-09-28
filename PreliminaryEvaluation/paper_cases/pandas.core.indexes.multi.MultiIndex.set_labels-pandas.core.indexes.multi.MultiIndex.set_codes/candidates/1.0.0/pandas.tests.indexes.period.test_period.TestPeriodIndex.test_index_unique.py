def test_index_unique(self):
    idx = PeriodIndex([2000, 2007, 2007, 2009, 2009], freq='A-JUN')
    expected = PeriodIndex([2000, 2007, 2009], freq='A-JUN')
    tm.assert_index_equal(idx.unique(), expected)
    assert idx.nunique() == 3
    idx = PeriodIndex([2000, 2007, 2007, 2009, 2007], freq='A-JUN', tz='US/Eastern')
    expected = PeriodIndex([2000, 2007, 2009], freq='A-JUN', tz='US/Eastern')
    tm.assert_index_equal(idx.unique(), expected)
    assert idx.nunique() == 3