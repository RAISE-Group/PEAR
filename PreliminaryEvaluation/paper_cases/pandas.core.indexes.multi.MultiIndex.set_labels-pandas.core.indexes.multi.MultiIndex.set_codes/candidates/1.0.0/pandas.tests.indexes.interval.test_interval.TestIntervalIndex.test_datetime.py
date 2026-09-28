@pytest.mark.parametrize('tz', [None, 'US/Eastern'])
def test_datetime(self, tz):
    start = Timestamp('2000-01-01', tz=tz)
    dates = date_range(start=start, periods=10)
    index = IntervalIndex.from_breaks(dates)
    start = Timestamp('2000-01-01T12:00', tz=tz)
    expected = date_range(start=start, periods=9)
    tm.assert_index_equal(index.mid, expected)
    assert Timestamp('2000-01-01', tz=tz) not in index
    assert Timestamp('2000-01-01T12', tz=tz) not in index
    assert Timestamp('2000-01-02', tz=tz) not in index
    iv_true = Interval(Timestamp('2000-01-02', tz=tz), Timestamp('2000-01-03', tz=tz))
    iv_false = Interval(Timestamp('1999-12-31', tz=tz), Timestamp('2000-01-01', tz=tz))
    assert iv_true in index
    assert iv_false not in index
    assert not index.contains(Timestamp('2000-01-01', tz=tz)).any()
    assert index.contains(Timestamp('2000-01-01T12', tz=tz)).any()
    assert index.contains(Timestamp('2000-01-02', tz=tz)).any()
    start = Timestamp('1999-12-31T12:00', tz=tz)
    target = date_range(start=start, periods=7, freq='12H')
    actual = index.get_indexer(target)
    expected = np.array([-1, -1, 0, 0, 1, 1, 2], dtype='intp')
    tm.assert_numpy_array_equal(actual, expected)
    start = Timestamp('2000-01-08T18:00', tz=tz)
    target = date_range(start=start, periods=7, freq='6H')
    actual = index.get_indexer(target)
    expected = np.array([7, 7, 8, 8, 8, 8, -1], dtype='intp')
    tm.assert_numpy_array_equal(actual, expected)