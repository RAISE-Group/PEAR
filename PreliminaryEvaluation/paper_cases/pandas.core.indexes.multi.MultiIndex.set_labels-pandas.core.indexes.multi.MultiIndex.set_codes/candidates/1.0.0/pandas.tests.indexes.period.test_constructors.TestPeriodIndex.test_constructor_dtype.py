def test_constructor_dtype(self):
    idx = PeriodIndex(['2013-01', '2013-03'], dtype='period[M]')
    exp = PeriodIndex(['2013-01', '2013-03'], freq='M')
    tm.assert_index_equal(idx, exp)
    assert idx.dtype == 'period[M]'
    idx = PeriodIndex(['2013-01-05', '2013-03-05'], dtype='period[3D]')
    exp = PeriodIndex(['2013-01-05', '2013-03-05'], freq='3D')
    tm.assert_index_equal(idx, exp)
    assert idx.dtype == 'period[3D]'
    idx = PeriodIndex(['2013-01-01', '2013-01-02'], freq='D')
    res = PeriodIndex(idx, dtype='period[M]')
    exp = PeriodIndex(['2013-01', '2013-01'], freq='M')
    tm.assert_index_equal(res, exp)
    assert res.dtype == 'period[M]'
    res = PeriodIndex(idx, freq='M')
    tm.assert_index_equal(res, exp)
    assert res.dtype == 'period[M]'
    msg = 'specified freq and dtype are different'
    with pytest.raises(IncompatibleFrequency, match=msg):
        PeriodIndex(['2011-01'], freq='M', dtype='period[D]')