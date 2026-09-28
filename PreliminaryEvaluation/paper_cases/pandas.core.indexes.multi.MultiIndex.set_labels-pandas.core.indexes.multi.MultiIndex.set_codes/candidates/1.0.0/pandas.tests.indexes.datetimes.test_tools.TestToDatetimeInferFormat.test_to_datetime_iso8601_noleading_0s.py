@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_iso8601_noleading_0s(self, cache):
    s = pd.Series(['2014-1-1', '2014-2-2', '2015-3-3'])
    expected = pd.Series([pd.Timestamp('2014-01-01'), pd.Timestamp('2014-02-02'), pd.Timestamp('2015-03-03')])
    tm.assert_series_equal(pd.to_datetime(s, cache=cache), expected)
    tm.assert_series_equal(pd.to_datetime(s, format='%Y-%m-%d', cache=cache), expected)