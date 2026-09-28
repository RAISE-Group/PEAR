@pytest.mark.parametrize('start_end', [('2018-01-01T00:00:01.000Z', '2018-01-03T00:00:01.000Z'), ('2018-01-01T00:00:00.010Z', '2018-01-03T00:00:00.010Z'), ('2001-01-01T00:00:00.010Z', '2001-01-03T00:00:00.010Z')])
def test_range_with_millisecond_resolution(self, start_end):
    start, end = start_end
    result = pd.date_range(start=start, end=end, periods=2, closed='left')
    expected = DatetimeIndex([start])
    tm.assert_index_equal(result, expected)