def test_partition_sep_kwarg(self):
    values = Series(['a_b_c', 'c_d_e', np.nan, 'f_g_h'])
    expected = values.str.partition(sep='_')
    result = values.str.partition('_')
    tm.assert_frame_equal(result, expected)
    expected = values.str.rpartition(sep='_')
    result = values.str.rpartition('_')
    tm.assert_frame_equal(result, expected)