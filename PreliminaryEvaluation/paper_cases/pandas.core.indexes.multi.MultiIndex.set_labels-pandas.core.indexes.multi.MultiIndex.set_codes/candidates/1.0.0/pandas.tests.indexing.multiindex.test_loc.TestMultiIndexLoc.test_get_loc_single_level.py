def test_get_loc_single_level(self, single_level_multiindex):
    single_level = single_level_multiindex
    s = Series(np.random.randn(len(single_level)), index=single_level)
    for k in single_level.values:
        s[k]