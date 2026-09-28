def test_take(self):
    idx1 = pd.period_range('2011-01-01', '2011-01-31', freq='D', name='idx')
    for idx in [idx1]:
        result = idx.take([0])
        assert result == pd.Period('2011-01-01', freq='D')
        result = idx.take([5])
        assert result == pd.Period('2011-01-06', freq='D')
        result = idx.take([0, 1, 2])
        expected = pd.period_range('2011-01-01', '2011-01-03', freq='D', name='idx')
        tm.assert_index_equal(result, expected)
        assert result.freq == 'D'
        assert result.freq == expected.freq
        result = idx.take([0, 2, 4])
        expected = pd.PeriodIndex(['2011-01-01', '2011-01-03', '2011-01-05'], freq='D', name='idx')
        tm.assert_index_equal(result, expected)
        assert result.freq == expected.freq
        assert result.freq == 'D'
        result = idx.take([7, 4, 1])
        expected = pd.PeriodIndex(['2011-01-08', '2011-01-05', '2011-01-02'], freq='D', name='idx')
        tm.assert_index_equal(result, expected)
        assert result.freq == expected.freq
        assert result.freq == 'D'
        result = idx.take([3, 2, 5])
        expected = PeriodIndex(['2011-01-04', '2011-01-03', '2011-01-06'], freq='D', name='idx')
        tm.assert_index_equal(result, expected)
        assert result.freq == expected.freq
        assert result.freq == 'D'
        result = idx.take([-3, 2, 5])
        expected = PeriodIndex(['2011-01-29', '2011-01-03', '2011-01-06'], freq='D', name='idx')
        tm.assert_index_equal(result, expected)
        assert result.freq == expected.freq
        assert result.freq == 'D'