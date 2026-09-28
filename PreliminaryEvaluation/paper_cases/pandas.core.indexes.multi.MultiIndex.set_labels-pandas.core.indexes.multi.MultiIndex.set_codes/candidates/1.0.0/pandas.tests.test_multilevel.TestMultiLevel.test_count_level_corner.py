def test_count_level_corner(self):
    s = self.frame['A'][:0]
    result = s.count(level=0)
    expected = Series(0, index=s.index.levels[0], name='A')
    tm.assert_series_equal(result, expected)
    df = self.frame[:0]
    result = df.count(level=0)
    expected = DataFrame(index=s.index.levels[0].set_names(['first']), columns=df.columns).fillna(0).astype(np.int64)
    tm.assert_frame_equal(result, expected)