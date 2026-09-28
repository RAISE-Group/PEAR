def test_groupby_levels_and_columns(self):
    idx_names = ['x', 'y']
    idx = pd.MultiIndex.from_tuples([(1, 1), (1, 2), (3, 4), (5, 6)], names=idx_names)
    df = pd.DataFrame(np.arange(12).reshape(-1, 3), index=idx)
    by_levels = df.groupby(level=idx_names).mean()
    by_columns = df.reset_index().groupby(idx_names).mean()
    tm.assert_frame_equal(by_levels, by_columns, check_column_type=False)
    by_columns.columns = pd.Index(by_columns.columns, dtype=np.int64)
    tm.assert_frame_equal(by_levels, by_columns)