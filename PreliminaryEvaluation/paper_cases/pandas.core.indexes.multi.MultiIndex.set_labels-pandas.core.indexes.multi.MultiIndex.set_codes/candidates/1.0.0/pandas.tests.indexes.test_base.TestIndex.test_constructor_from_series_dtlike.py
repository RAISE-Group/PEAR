@pytest.mark.parametrize('index,has_tz', [(pd.date_range('2015-01-01 10:00', freq='D', periods=3, tz='US/Eastern'), True), (pd.timedelta_range('1 days', freq='D', periods=3), False), (pd.period_range('2015-01-01', freq='D', periods=3), False)])
def test_constructor_from_series_dtlike(self, index, has_tz):
    result = pd.Index(pd.Series(index))
    tm.assert_index_equal(result, index)
    if has_tz:
        assert result.tz == index.tz