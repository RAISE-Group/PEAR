def test_basic_drop_first_NA(self, sparse):
    s_NA = ['a', 'b', np.nan]
    res = get_dummies(s_NA, drop_first=True, sparse=sparse)
    exp = DataFrame({'b': [0, 1, 0]}, dtype=np.uint8)
    if sparse:
        exp = exp.apply(SparseArray, fill_value=0)
    tm.assert_frame_equal(res, exp)
    res_na = get_dummies(s_NA, dummy_na=True, drop_first=True, sparse=sparse)
    exp_na = DataFrame({'b': [0, 1, 0], np.nan: [0, 0, 1]}, dtype=np.uint8).reindex(['b', np.nan], axis=1)
    if sparse:
        exp_na = exp_na.apply(SparseArray, fill_value=0)
    tm.assert_frame_equal(res_na, exp_na)
    res_just_na = get_dummies([np.nan], dummy_na=True, drop_first=True, sparse=sparse)
    exp_just_na = DataFrame(index=np.arange(1))
    tm.assert_frame_equal(res_just_na, exp_just_na)