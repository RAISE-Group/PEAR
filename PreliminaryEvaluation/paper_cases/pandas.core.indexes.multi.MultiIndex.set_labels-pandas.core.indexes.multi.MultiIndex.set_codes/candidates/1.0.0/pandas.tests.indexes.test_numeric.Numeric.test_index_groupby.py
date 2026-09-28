def test_index_groupby(self):
    int_idx = Index(range(6))
    float_idx = Index(np.arange(0, 0.6, 0.1))
    obj_idx = Index('A B C D E F'.split())
    dt_idx = pd.date_range('2013-01-01', freq='M', periods=6)
    for idx in [int_idx, float_idx, obj_idx, dt_idx]:
        to_groupby = np.array([1, 2, np.nan, np.nan, 2, 1])
        tm.assert_dict_equal(idx.groupby(to_groupby), {1.0: idx[[0, 5]], 2.0: idx[[1, 4]]})
        to_groupby = Index([datetime(2011, 11, 1), datetime(2011, 12, 1), pd.NaT, pd.NaT, datetime(2011, 12, 1), datetime(2011, 11, 1)], tz='UTC').values
        ex_keys = [Timestamp('2011-11-01'), Timestamp('2011-12-01')]
        expected = {ex_keys[0]: idx[[0, 5]], ex_keys[1]: idx[[1, 4]]}
        tm.assert_dict_equal(idx.groupby(to_groupby), expected)