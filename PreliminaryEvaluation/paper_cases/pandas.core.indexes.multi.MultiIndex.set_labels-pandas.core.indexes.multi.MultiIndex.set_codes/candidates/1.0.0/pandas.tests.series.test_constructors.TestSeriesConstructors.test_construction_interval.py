@pytest.mark.parametrize('interval_constructor', [IntervalIndex, IntervalArray])
def test_construction_interval(self, interval_constructor):
    intervals = interval_constructor.from_breaks(np.arange(3), closed='right')
    result = Series(intervals)
    assert result.dtype == 'interval[int64]'
    tm.assert_index_equal(Index(result.values), Index(intervals))