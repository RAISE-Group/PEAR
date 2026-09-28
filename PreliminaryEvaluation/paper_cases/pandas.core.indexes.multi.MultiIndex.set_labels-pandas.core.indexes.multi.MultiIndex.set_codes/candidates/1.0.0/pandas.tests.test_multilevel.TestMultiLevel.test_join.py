def test_join(self):
    a = self.frame.loc[self.frame.index[:5], ['A']]
    b = self.frame.loc[self.frame.index[2:], ['B', 'C']]
    joined = a.join(b, how='outer').reindex(self.frame.index)
    expected = self.frame.copy()
    expected.values[np.isnan(joined.values)] = np.nan
    assert not np.isnan(joined.values).all()
    tm.assert_frame_equal(joined, expected, check_names=False)