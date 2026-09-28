def test_partition_index(self):
    values = Index(['a_b_c', 'c_d_e', 'f_g_h', np.nan, None])
    result = values.str.partition('_', expand=False)
    exp = Index(np.array([('a', '_', 'b_c'), ('c', '_', 'd_e'), ('f', '_', 'g_h'), np.nan, None], dtype=object))
    tm.assert_index_equal(result, exp)
    assert result.nlevels == 1
    result = values.str.rpartition('_', expand=False)
    exp = Index(np.array([('a_b', '_', 'c'), ('c_d', '_', 'e'), ('f_g', '_', 'h'), np.nan, None], dtype=object))
    tm.assert_index_equal(result, exp)
    assert result.nlevels == 1
    result = values.str.partition('_')
    exp = Index([('a', '_', 'b_c'), ('c', '_', 'd_e'), ('f', '_', 'g_h'), (np.nan, np.nan, np.nan), (None, None, None)])
    tm.assert_index_equal(result, exp)
    assert isinstance(result, MultiIndex)
    assert result.nlevels == 3
    result = values.str.rpartition('_')
    exp = Index([('a_b', '_', 'c'), ('c_d', '_', 'e'), ('f_g', '_', 'h'), (np.nan, np.nan, np.nan), (None, None, None)])
    tm.assert_index_equal(result, exp)
    assert isinstance(result, MultiIndex)
    assert result.nlevels == 3