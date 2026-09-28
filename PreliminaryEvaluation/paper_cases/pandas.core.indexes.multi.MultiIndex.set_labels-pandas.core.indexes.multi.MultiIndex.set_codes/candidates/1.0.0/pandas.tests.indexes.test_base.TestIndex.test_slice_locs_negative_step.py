@pytest.mark.parametrize('in_slice,expected', [(pd.IndexSlice[::-1], 'yxdcb'), (pd.IndexSlice['b':'y':-1], ''), (pd.IndexSlice['b'::-1], 'b'), (pd.IndexSlice[:'b':-1], 'yxdcb'), (pd.IndexSlice[:'y':-1], 'y'), (pd.IndexSlice['y'::-1], 'yxdcb'), (pd.IndexSlice['y'::-4], 'yb'), (pd.IndexSlice[:'a':-1], 'yxdcb'), (pd.IndexSlice[:'a':-2], 'ydb'), (pd.IndexSlice['z'::-1], 'yxdcb'), (pd.IndexSlice['z'::-3], 'yc'), (pd.IndexSlice['m'::-1], 'dcb'), (pd.IndexSlice[:'m':-1], 'yx'), (pd.IndexSlice['a':'a':-1], ''), (pd.IndexSlice['z':'z':-1], ''), (pd.IndexSlice['m':'m':-1], '')])
def test_slice_locs_negative_step(self, in_slice, expected):
    index = Index(list('bcdxy'))
    s_start, s_stop = index.slice_locs(in_slice.start, in_slice.stop, in_slice.step)
    result = index[s_start:s_stop:in_slice.step]
    expected = pd.Index(list(expected))
    tm.assert_index_equal(result, expected)