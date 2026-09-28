@pytest.mark.parametrize('start, mid, end', [(Timestamp('2018-03-10', tz='US/Eastern'), Timestamp('2018-03-10 23:30:00', tz='US/Eastern'), Timestamp('2018-03-12', tz='US/Eastern')), (Timestamp('2018-11-03', tz='US/Eastern'), Timestamp('2018-11-04 00:30:00', tz='US/Eastern'), Timestamp('2018-11-05', tz='US/Eastern'))])
def test_linspace_dst_transition(self, start, mid, end):
    result = interval_range(start=start, end=end, periods=2)
    expected = IntervalIndex.from_breaks([start, mid, end])
    tm.assert_index_equal(result, expected)