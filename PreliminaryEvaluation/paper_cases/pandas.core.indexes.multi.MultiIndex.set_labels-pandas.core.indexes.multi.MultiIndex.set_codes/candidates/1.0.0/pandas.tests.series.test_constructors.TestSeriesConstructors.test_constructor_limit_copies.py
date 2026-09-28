@pytest.mark.parametrize('index', [pd.date_range('20170101', periods=3, tz='US/Eastern'), pd.date_range('20170101', periods=3), pd.timedelta_range('1 day', periods=3), pd.period_range('2012Q1', periods=3, freq='Q'), pd.Index(list('abc')), pd.Int64Index([1, 2, 3]), pd.RangeIndex(0, 3)], ids=lambda x: type(x).__name__)
def test_constructor_limit_copies(self, index):
    s = pd.Series(index)
    assert s._data.blocks[0].values is not index