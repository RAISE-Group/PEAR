def test_slice_with_negative_step(self):
    ts = Series(np.arange(20), period_range('2014-01', periods=20, freq='M'))
    SLC = pd.IndexSlice

    def assert_slices_equivalent(l_slc, i_slc):
        tm.assert_series_equal(ts[l_slc], ts.iloc[i_slc])
        tm.assert_series_equal(ts.loc[l_slc], ts.iloc[i_slc])
        tm.assert_series_equal(ts.loc[l_slc], ts.iloc[i_slc])
    assert_slices_equivalent(SLC[Period('2014-10')::-1], SLC[9::-1])
    assert_slices_equivalent(SLC['2014-10'::-1], SLC[9::-1])
    assert_slices_equivalent(SLC[:Period('2014-10'):-1], SLC[:8:-1])
    assert_slices_equivalent(SLC[:'2014-10':-1], SLC[:8:-1])
    assert_slices_equivalent(SLC['2015-02':'2014-10':-1], SLC[13:8:-1])
    assert_slices_equivalent(SLC[Period('2015-02'):Period('2014-10'):-1], SLC[13:8:-1])
    assert_slices_equivalent(SLC['2015-02':Period('2014-10'):-1], SLC[13:8:-1])
    assert_slices_equivalent(SLC[Period('2015-02'):'2014-10':-1], SLC[13:8:-1])
    assert_slices_equivalent(SLC['2014-10':'2015-02':-1], SLC[:0])