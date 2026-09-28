@pytest.mark.parametrize('case', [[pd.Timestamp('2011-01-01'), pd.Timestamp('2011-01-02'), pd.Timestamp('2011-01-03')], [pd.Timestamp('2011-01-01', tz='US/Eastern'), pd.Timestamp('2011-01-02', tz='US/Eastern'), pd.Timestamp('2011-01-03', tz='US/Eastern')], [pd.Timedelta('1 days'), pd.Timedelta('2 days'), pd.Timedelta('3 days')], [pd.Timestamp('2011-01-01'), pd.Timestamp('2011-01-02'), pd.Timestamp('2011-01-03'), pd.NaT], [pd.Timestamp('2011-01-01', tz='US/Eastern'), pd.Timestamp('2011-01-02', tz='US/Eastern'), pd.Timestamp('2011-01-03', tz='US/Eastern'), pd.NaT], [pd.Timedelta('1 days'), pd.Timedelta('2 days'), pd.Timedelta('3 days'), pd.NaT]])
def test_quantile_box(self, case):
    s = pd.Series(case, name='XXX')
    res = s.quantile(0.5)
    assert res == case[1]
    res = s.quantile([0.5])
    exp = pd.Series([case[1]], index=[0.5], name='XXX')
    tm.assert_series_equal(res, exp)