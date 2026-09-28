def test_take(self):
    idx1 = pd.date_range('2011-01-01', '2011-01-31', freq='D', name='idx')
    idx2 = pd.date_range('2011-01-01', '2011-01-31', freq='D', tz='Asia/Tokyo', name='idx')
    for idx in [idx1, idx2]:
        result = idx.take([0])
        assert result == Timestamp('2011-01-01', tz=idx.tz)
        result = idx.take([0, 1, 2])
        expected = pd.date_range('2011-01-01', '2011-01-03', freq='D', tz=idx.tz, name='idx')
        tm.assert_index_equal(result, expected)
        assert result.freq == expected.freq
        result = idx.take([0, 2, 4])
        expected = pd.date_range('2011-01-01', '2011-01-05', freq='2D', tz=idx.tz, name='idx')
        tm.assert_index_equal(result, expected)
        assert result.freq == expected.freq
        result = idx.take([7, 4, 1])
        expected = pd.date_range('2011-01-08', '2011-01-02', freq='-3D', tz=idx.tz, name='idx')
        tm.assert_index_equal(result, expected)
        assert result.freq == expected.freq
        result = idx.take([3, 2, 5])
        expected = DatetimeIndex(['2011-01-04', '2011-01-03', '2011-01-06'], freq=None, tz=idx.tz, name='idx')
        tm.assert_index_equal(result, expected)
        assert result.freq is None
        result = idx.take([-3, 2, 5])
        expected = DatetimeIndex(['2011-01-29', '2011-01-03', '2011-01-06'], freq=None, tz=idx.tz, name='idx')
        tm.assert_index_equal(result, expected)
        assert result.freq is None