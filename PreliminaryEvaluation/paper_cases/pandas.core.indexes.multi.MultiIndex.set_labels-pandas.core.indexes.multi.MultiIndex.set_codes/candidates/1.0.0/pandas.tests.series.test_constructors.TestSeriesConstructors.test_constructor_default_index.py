def test_constructor_default_index(self):
    s = Series([0, 1, 2])
    tm.assert_index_equal(s.index, pd.Index(np.arange(3)))