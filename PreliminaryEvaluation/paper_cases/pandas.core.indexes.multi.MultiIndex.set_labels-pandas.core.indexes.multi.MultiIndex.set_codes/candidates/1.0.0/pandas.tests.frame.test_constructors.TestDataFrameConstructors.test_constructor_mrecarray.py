def test_constructor_mrecarray(self):
    assert_fr_equal = functools.partial(tm.assert_frame_equal, check_index_type=True, check_column_type=True, check_frame_type=True)
    arrays = [('float', np.array([1.5, 2.0])), ('int', np.array([1, 2])), ('str', np.array(['abc', 'def']))]
    for name, arr in arrays[:]:
        arrays.append(('masked1_' + name, np.ma.masked_array(arr, mask=[False, True])))
    arrays.append(('masked_all', np.ma.masked_all((2,))))
    arrays.append(('masked_none', np.ma.masked_array([1.0, 2.5], mask=False)))
    for comb in itertools.combinations(arrays, 3):
        names, data = zip(*comb)
        mrecs = mrecords.fromarrays(data, names=names)
        comb = {k: v.filled() if hasattr(v, 'filled') else v for k, v in comb}
        expected = DataFrame(comb, columns=names)
        result = DataFrame(mrecs)
        assert_fr_equal(result, expected)
        expected = DataFrame(comb, columns=names[::-1])
        result = DataFrame(mrecs, columns=names[::-1])
        assert_fr_equal(result, expected)
        expected = DataFrame(comb, columns=names, index=[1, 2])
        result = DataFrame(mrecs, index=[1, 2])
        assert_fr_equal(result, expected)