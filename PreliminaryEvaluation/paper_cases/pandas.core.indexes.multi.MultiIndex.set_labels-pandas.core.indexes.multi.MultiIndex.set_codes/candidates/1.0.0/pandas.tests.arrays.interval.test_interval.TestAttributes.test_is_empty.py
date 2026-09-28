@pytest.mark.parametrize('left, right', [(0, 1), (Timedelta('0 days'), Timedelta('1 day')), (Timestamp('2018-01-01'), Timestamp('2018-01-02')), (Timestamp('2018-01-01', tz='US/Eastern'), Timestamp('2018-01-02', tz='US/Eastern'))])
@pytest.mark.parametrize('constructor', [IntervalArray, IntervalIndex])
def test_is_empty(self, constructor, left, right, closed):
    tuples = [(left, left), (left, right), np.nan]
    expected = np.array([closed != 'both', False, False])
    result = constructor.from_tuples(tuples, closed=closed).is_empty
    tm.assert_numpy_array_equal(result, expected)