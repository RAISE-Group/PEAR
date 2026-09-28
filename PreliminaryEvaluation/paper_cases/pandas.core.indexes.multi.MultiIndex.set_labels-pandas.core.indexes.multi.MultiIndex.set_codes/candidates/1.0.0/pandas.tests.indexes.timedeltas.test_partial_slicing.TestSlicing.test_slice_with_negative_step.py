def test_slice_with_negative_step(self):
    ts = Series(np.arange(20), timedelta_range('0', periods=20, freq='H'))
    SLC = pd.IndexSlice

    def assert_slices_equivalent(l_slc, i_slc):
        tm.assert_series_equal(ts[l_slc], ts.iloc[i_slc])
        tm.assert_series_equal(ts.loc[l_slc], ts.iloc[i_slc])
        tm.assert_series_equal(ts.loc[l_slc], ts.iloc[i_slc])
    assert_slices_equivalent(SLC[Timedelta(hours=7)::-1], SLC[7::-1])
    assert_slices_equivalent(SLC['7 hours'::-1], SLC[7::-1])
    assert_slices_equivalent(SLC[:Timedelta(hours=7):-1], SLC[:6:-1])
    assert_slices_equivalent(SLC[:'7 hours':-1], SLC[:6:-1])
    assert_slices_equivalent(SLC['15 hours':'7 hours':-1], SLC[15:6:-1])
    assert_slices_equivalent(SLC[Timedelta(hours=15):Timedelta(hours=7):-1], SLC[15:6:-1])
    assert_slices_equivalent(SLC['15 hours':Timedelta(hours=7):-1], SLC[15:6:-1])
    assert_slices_equivalent(SLC[Timedelta(hours=15):'7 hours':-1], SLC[15:6:-1])
    assert_slices_equivalent(SLC['7 hours':'15 hours':-1], SLC[:0])