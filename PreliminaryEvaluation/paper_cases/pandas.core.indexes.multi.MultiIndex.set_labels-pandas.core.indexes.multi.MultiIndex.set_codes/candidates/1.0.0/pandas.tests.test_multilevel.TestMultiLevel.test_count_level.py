def test_count_level(self):

    def _check_counts(frame, axis=0):
        index = frame._get_axis(axis)
        for i in range(index.nlevels):
            result = frame.count(axis=axis, level=i)
            expected = frame.groupby(axis=axis, level=i).count()
            expected = expected.reindex_like(result).astype('i8')
            tm.assert_frame_equal(result, expected)
    self.frame.iloc[1, [1, 2]] = np.nan
    self.frame.iloc[7, [0, 1]] = np.nan
    self.ymd.iloc[1, [1, 2]] = np.nan
    self.ymd.iloc[7, [0, 1]] = np.nan
    _check_counts(self.frame)
    _check_counts(self.ymd)
    _check_counts(self.frame.T, axis=1)
    _check_counts(self.ymd.T, axis=1)
    df = tm.makeTimeDataFrame()
    with pytest.raises(TypeError, match='hierarchical'):
        df.count(level=0)
    self.frame['D'] = 'foo'
    result = self.frame.count(level=0, numeric_only=True)
    tm.assert_index_equal(result.columns, Index(list('ABC'), name='exp'))