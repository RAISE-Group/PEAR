def test_shift_corner_cases(self):
    idx = pd.PeriodIndex([], name='xxx', freq='H')
    with pytest.raises(TypeError):
        idx.shift(1, freq='H')
    tm.assert_index_equal(idx.shift(0), idx)
    tm.assert_index_equal(idx.shift(3), idx)
    idx = pd.PeriodIndex(['2011-01-01 10:00', '2011-01-01 11:00', '2011-01-01 12:00'], name='xxx', freq='H')
    tm.assert_index_equal(idx.shift(0), idx)
    exp = pd.PeriodIndex(['2011-01-01 13:00', '2011-01-01 14:00', '2011-01-01 15:00'], name='xxx', freq='H')
    tm.assert_index_equal(idx.shift(3), exp)
    exp = pd.PeriodIndex(['2011-01-01 07:00', '2011-01-01 08:00', '2011-01-01 09:00'], name='xxx', freq='H')
    tm.assert_index_equal(idx.shift(-3), exp)