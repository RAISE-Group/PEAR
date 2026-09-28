@pytest.mark.parametrize('method, dates', [['round', ['2012-01-02', '2012-01-02', '2012-01-01']], ['floor', ['2012-01-01', '2012-01-01', '2012-01-01']], ['ceil', ['2012-01-02', '2012-01-02', '2012-01-02']]])
def test_dt_round(self, method, dates):
    s = Series(pd.to_datetime(['2012-01-01 13:00:00', '2012-01-01 12:01:00', '2012-01-01 08:00:00']), name='xxx')
    result = getattr(s.dt, method)('D')
    expected = Series(pd.to_datetime(dates), name='xxx')
    tm.assert_series_equal(result, expected)