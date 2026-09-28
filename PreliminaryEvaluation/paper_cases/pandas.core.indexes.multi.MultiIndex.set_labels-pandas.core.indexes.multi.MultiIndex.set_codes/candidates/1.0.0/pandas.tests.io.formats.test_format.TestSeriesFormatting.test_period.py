def test_period(self):
    index = pd.period_range('2013-01', periods=6, freq='M')
    s = Series(np.arange(6, dtype='int64'), index=index)
    exp = '2013-01    0\n2013-02    1\n2013-03    2\n2013-04    3\n2013-05    4\n2013-06    5\nFreq: M, dtype: int64'
    assert str(s) == exp
    s = Series(index)
    exp = '0    2013-01\n1    2013-02\n2    2013-03\n3    2013-04\n4    2013-05\n5    2013-06\ndtype: period[M]'
    assert str(s) == exp
    s = Series([pd.Period('2011-01', freq='M'), pd.Period('2011-02-01', freq='D'), pd.Period('2011-03-01 09:00', freq='H')])
    exp = '0             2011-01\n1          2011-02-01\n2    2011-03-01 09:00\ndtype: object'
    assert str(s) == exp