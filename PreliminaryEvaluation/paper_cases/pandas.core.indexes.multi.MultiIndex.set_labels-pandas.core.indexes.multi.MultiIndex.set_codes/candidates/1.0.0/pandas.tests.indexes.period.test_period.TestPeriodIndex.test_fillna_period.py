def test_fillna_period(self):
    idx = pd.PeriodIndex(['2011-01-01 09:00', pd.NaT, '2011-01-01 11:00'], freq='H')
    exp = pd.PeriodIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], freq='H')
    tm.assert_index_equal(idx.fillna(pd.Period('2011-01-01 10:00', freq='H')), exp)
    exp = pd.Index([pd.Period('2011-01-01 09:00', freq='H'), 'x', pd.Period('2011-01-01 11:00', freq='H')], dtype=object)
    tm.assert_index_equal(idx.fillna('x'), exp)
    exp = pd.Index([pd.Period('2011-01-01 09:00', freq='H'), pd.Period('2011-01-01', freq='D'), pd.Period('2011-01-01 11:00', freq='H')], dtype=object)
    tm.assert_index_equal(idx.fillna(pd.Period('2011-01-01', freq='D')), exp)