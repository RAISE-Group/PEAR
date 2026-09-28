@pytest.mark.parametrize('data', [interval_range(0, periods=10, closed='neither'), interval_range(1.7, periods=8, freq=2.5, closed='both'), interval_range(Timestamp('20170101'), periods=12, closed='left'), interval_range(Timedelta('1 day'), periods=6, closed='right')])
def test_insert(self, data):
    item = data[0]
    idx_item = IntervalIndex([item])
    expected = idx_item.append(data)
    result = data.insert(0, item)
    tm.assert_index_equal(result, expected)
    expected = data.append(idx_item)
    result = data.insert(len(data), item)
    tm.assert_index_equal(result, expected)
    expected = data[:3].append(idx_item).append(data[3:])
    result = data.insert(3, item)
    tm.assert_index_equal(result, expected)
    msg = 'can only insert Interval objects and NA into an IntervalIndex'
    with pytest.raises(ValueError, match=msg):
        data.insert(1, 'foo')
    msg = 'inserted item must be closed on the same side as the index'
    for closed in {'left', 'right', 'both', 'neither'} - {item.closed}:
        with pytest.raises(ValueError, match=msg):
            bad_item = Interval(item.left, item.right, closed=closed)
            data.insert(1, bad_item)
    na_idx = IntervalIndex([np.nan], closed=data.closed)
    for na in (np.nan, pd.NaT, None):
        expected = data[:1].append(na_idx).append(data[1:])
        result = data.insert(1, na)
        tm.assert_index_equal(result, expected)