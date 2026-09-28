def test_reset_index_period(self):
    idx = MultiIndex.from_product([pd.period_range('20130101', periods=3, freq='M'), list('abc')], names=['month', 'feature'])
    df = DataFrame(np.arange(9, dtype='int64').reshape(-1, 1), index=idx, columns=['a'])
    expected = DataFrame({'month': [pd.Period('2013-01', freq='M')] * 3 + [pd.Period('2013-02', freq='M')] * 3 + [pd.Period('2013-03', freq='M')] * 3, 'feature': ['a', 'b', 'c'] * 3, 'a': np.arange(9, dtype='int64')}, columns=['month', 'feature', 'a'])
    tm.assert_frame_equal(df.reset_index(), expected)