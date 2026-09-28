def test_str_label_slicing_with_negative_step(self):
    SLC = pd.IndexSlice

    def assert_slices_equivalent(l_slc, i_slc):
        tm.assert_series_equal(s.loc[l_slc], s.iloc[i_slc])
        if not idx.is_integer:
            tm.assert_series_equal(s[l_slc], s.iloc[i_slc])
            tm.assert_series_equal(s.loc[l_slc], s.iloc[i_slc])
    for idx in [_mklbl('A', 20), np.arange(20) + 100, np.linspace(100, 150, 20)]:
        idx = Index(idx)
        s = Series(np.arange(20), index=idx)
        assert_slices_equivalent(SLC[idx[9]::-1], SLC[9::-1])
        assert_slices_equivalent(SLC[:idx[9]:-1], SLC[:8:-1])
        assert_slices_equivalent(SLC[idx[13]:idx[9]:-1], SLC[13:8:-1])
        assert_slices_equivalent(SLC[idx[9]:idx[13]:-1], SLC[:0])