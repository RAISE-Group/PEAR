def test_multiindex_label_slicing_with_negative_step(self):
    s = Series(np.arange(20), MultiIndex.from_product([list('abcde'), np.arange(4)]))
    SLC = pd.IndexSlice

    def assert_slices_equivalent(l_slc, i_slc):
        tm.assert_series_equal(s.loc[l_slc], s.iloc[i_slc])
        tm.assert_series_equal(s[l_slc], s.iloc[i_slc])
    assert_slices_equivalent(SLC[::-1], SLC[::-1])
    assert_slices_equivalent(SLC['d'::-1], SLC[15::-1])
    assert_slices_equivalent(SLC[('d',)::-1], SLC[15::-1])
    assert_slices_equivalent(SLC[:'d':-1], SLC[:11:-1])
    assert_slices_equivalent(SLC[:('d',):-1], SLC[:11:-1])
    assert_slices_equivalent(SLC['d':'b':-1], SLC[15:3:-1])
    assert_slices_equivalent(SLC[('d',):'b':-1], SLC[15:3:-1])
    assert_slices_equivalent(SLC['d':('b',):-1], SLC[15:3:-1])
    assert_slices_equivalent(SLC[('d',):('b',):-1], SLC[15:3:-1])
    assert_slices_equivalent(SLC['b':'d':-1], SLC[:0])
    assert_slices_equivalent(SLC[('c', 2)::-1], SLC[10::-1])
    assert_slices_equivalent(SLC[:('c', 2):-1], SLC[:9:-1])
    assert_slices_equivalent(SLC[('e', 0):('c', 2):-1], SLC[16:9:-1])