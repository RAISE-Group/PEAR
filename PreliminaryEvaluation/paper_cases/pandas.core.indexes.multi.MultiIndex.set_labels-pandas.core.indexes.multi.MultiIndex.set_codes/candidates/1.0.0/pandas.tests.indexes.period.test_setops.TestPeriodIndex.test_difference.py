@pytest.mark.parametrize('sort', [None, False])
def test_difference(self, sort):
    period_rng = ['1/3/2000', '1/2/2000', '1/1/2000', '1/5/2000', '1/4/2000']
    rng1 = pd.PeriodIndex(period_rng, freq='D')
    other1 = pd.period_range('1/6/2000', freq='D', periods=5)
    expected1 = rng1
    rng2 = pd.PeriodIndex(period_rng, freq='D')
    other2 = pd.period_range('1/4/2000', freq='D', periods=5)
    expected2 = pd.PeriodIndex(['1/3/2000', '1/2/2000', '1/1/2000'], freq='D')
    rng3 = pd.PeriodIndex(period_rng, freq='D')
    other3 = pd.PeriodIndex([], freq='D')
    expected3 = rng3
    period_rng = ['2000-01-01 10:00', '2000-01-01 09:00', '2000-01-01 12:00', '2000-01-01 11:00', '2000-01-01 13:00']
    rng4 = pd.PeriodIndex(period_rng, freq='H')
    other4 = pd.period_range('2000-01-02 09:00', freq='H', periods=5)
    expected4 = rng4
    rng5 = pd.PeriodIndex(['2000-01-01 09:03', '2000-01-01 09:01', '2000-01-01 09:05'], freq='T')
    other5 = pd.PeriodIndex(['2000-01-01 09:01', '2000-01-01 09:05'], freq='T')
    expected5 = pd.PeriodIndex(['2000-01-01 09:03'], freq='T')
    period_rng = ['2000-02-01', '2000-01-01', '2000-06-01', '2000-07-01', '2000-05-01', '2000-03-01', '2000-04-01']
    rng6 = pd.PeriodIndex(period_rng, freq='M')
    other6 = pd.period_range('2000-04-01', freq='M', periods=7)
    expected6 = pd.PeriodIndex(['2000-02-01', '2000-01-01', '2000-03-01'], freq='M')
    period_rng = ['2003', '2007', '2006', '2005', '2004']
    rng7 = pd.PeriodIndex(period_rng, freq='A')
    other7 = pd.period_range('1998-01-01', freq='A', periods=8)
    expected7 = pd.PeriodIndex(['2007', '2006'], freq='A')
    for rng, other, expected in [(rng1, other1, expected1), (rng2, other2, expected2), (rng3, other3, expected3), (rng4, other4, expected4), (rng5, other5, expected5), (rng6, other6, expected6), (rng7, other7, expected7)]:
        result_difference = rng.difference(other, sort=sort)
        if sort is None:
            expected = expected.sort_values()
        tm.assert_index_equal(result_difference, expected)