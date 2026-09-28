@pytest.mark.parametrize('index_dates,expected_dates', [(['2011-01-01', '2011-01-03', '2011-01-05', '2011-01-02', '2011-01-01'], ['2011-01-01', '2011-01-01', '2011-01-02', '2011-01-03', '2011-01-05']), (['2011-01-01', '2011-01-03', '2011-01-05', '2011-01-02', '2011-01-01'], ['2011-01-01', '2011-01-01', '2011-01-02', '2011-01-03', '2011-01-05']), ([pd.NaT, '2011-01-03', '2011-01-05', '2011-01-02', pd.NaT], [pd.NaT, pd.NaT, '2011-01-02', '2011-01-03', '2011-01-05'])])
def test_order_without_freq(self, index_dates, expected_dates, tz_naive_fixture):
    tz = tz_naive_fixture
    index = DatetimeIndex(index_dates, tz=tz, name='idx')
    expected = DatetimeIndex(expected_dates, tz=tz, name='idx')
    ordered = index.sort_values()
    tm.assert_index_equal(ordered, expected)
    assert ordered.freq is None
    ordered = index.sort_values(ascending=False)
    tm.assert_index_equal(ordered, expected[::-1])
    assert ordered.freq is None
    ordered, indexer = index.sort_values(return_indexer=True)
    tm.assert_index_equal(ordered, expected)
    exp = np.array([0, 4, 3, 1, 2])
    tm.assert_numpy_array_equal(indexer, exp, check_dtype=False)
    assert ordered.freq is None
    ordered, indexer = index.sort_values(return_indexer=True, ascending=False)
    tm.assert_index_equal(ordered, expected[::-1])
    exp = np.array([2, 1, 3, 4, 0])
    tm.assert_numpy_array_equal(indexer, exp, check_dtype=False)
    assert ordered.freq is None