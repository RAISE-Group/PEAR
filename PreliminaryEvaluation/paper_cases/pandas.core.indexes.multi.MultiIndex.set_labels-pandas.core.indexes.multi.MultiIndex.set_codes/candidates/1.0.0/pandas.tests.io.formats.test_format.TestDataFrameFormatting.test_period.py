def test_period(self):
    df = pd.DataFrame({'A': pd.period_range('2013-01', periods=4, freq='M'), 'B': [pd.Period('2011-01', freq='M'), pd.Period('2011-02-01', freq='D'), pd.Period('2011-03-01 09:00', freq='H'), pd.Period('2011-04', freq='M')], 'C': list('abcd')})
    exp = '         A                 B  C\n0  2013-01           2011-01  a\n1  2013-02        2011-02-01  b\n2  2013-03  2011-03-01 09:00  c\n3  2013-04           2011-04  d'
    assert str(df) == exp