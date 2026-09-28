def test_unsorted_index(self):
    df = DataFrame({'y': np.arange(100)}, index=np.arange(99, -1, -1), dtype=np.int64)
    ax = df.plot()
    lines = ax.get_lines()[0]
    rs = lines.get_xydata()
    rs = Series(rs[:, 1], rs[:, 0], dtype=np.int64, name='y')
    tm.assert_series_equal(rs, df.y, check_index_type=False)
    tm.close()
    df.index = pd.Index(np.arange(99, -1, -1), dtype=np.float64)
    ax = df.plot()
    lines = ax.get_lines()[0]
    rs = lines.get_xydata()
    rs = Series(rs[:, 1], rs[:, 0], dtype=np.int64, name='y')
    tm.assert_series_equal(rs, df.y)