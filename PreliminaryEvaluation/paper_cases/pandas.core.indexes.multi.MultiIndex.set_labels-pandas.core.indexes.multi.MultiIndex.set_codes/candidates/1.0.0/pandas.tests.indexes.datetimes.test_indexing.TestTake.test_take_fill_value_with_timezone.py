def test_take_fill_value_with_timezone(self):
    idx = pd.DatetimeIndex(['2011-01-01', '2011-02-01', '2011-03-01'], name='xxx', tz='US/Eastern')
    result = idx.take(np.array([1, 0, -1]))
    expected = pd.DatetimeIndex(['2011-02-01', '2011-01-01', '2011-03-01'], name='xxx', tz='US/Eastern')
    tm.assert_index_equal(result, expected)
    result = idx.take(np.array([1, 0, -1]), fill_value=True)
    expected = pd.DatetimeIndex(['2011-02-01', '2011-01-01', 'NaT'], name='xxx', tz='US/Eastern')
    tm.assert_index_equal(result, expected)
    result = idx.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
    expected = pd.DatetimeIndex(['2011-02-01', '2011-01-01', '2011-03-01'], name='xxx', tz='US/Eastern')
    tm.assert_index_equal(result, expected)
    msg = 'When allow_fill=True and fill_value is not None, all indices must be >= -1'
    with pytest.raises(ValueError, match=msg):
        idx.take(np.array([1, 0, -2]), fill_value=True)
    with pytest.raises(ValueError, match=msg):
        idx.take(np.array([1, 0, -5]), fill_value=True)
    with pytest.raises(IndexError):
        idx.take(np.array([1, -5]))