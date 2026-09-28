@pytest.mark.parametrize('contents,dtype', [([-np.inf, -50, -1, -1e-20, -1e-25, -1e-50, 0, 1e-40, 1e-20, 1e-10, 2, 40, np.inf], 'float64'), ([-np.inf, -50, -1, -1e-20, -1e-25, -1e-45, 0, 1e-40, 1e-20, 1e-10, 2, 40, np.inf], 'float32'), ([np.iinfo(np.uint8).min, 1, 2, 100, np.iinfo(np.uint8).max], 'uint8'), pytest.param([np.iinfo(np.int64).min, -100, 0, 1, 9999, 100000, 10000000000.0, np.iinfo(np.int64).max], 'int64', marks=pytest.mark.xfail(reason='iNaT is equivalent to minimum value of dtypeint64 pending issue GH#16674')), ([NegInfinity(), '1', 'A', 'BA', 'Ba', 'C', Infinity()], 'object')])
def test_rank_inf(self, contents, dtype):
    dtype_na_map = {'float64': np.nan, 'float32': np.nan, 'int64': iNaT, 'object': None}
    values = np.array(contents, dtype=dtype)
    exp_order = np.array(range(len(values)), dtype='float64') + 1.0
    if dtype in dtype_na_map:
        na_value = dtype_na_map[dtype]
        nan_indices = np.random.choice(range(len(values)), 5)
        values = np.insert(values, nan_indices, na_value)
        exp_order = np.insert(exp_order, nan_indices, np.nan)
    random_order = np.random.permutation(len(values))
    iseries = Series(values[random_order])
    exp = Series(exp_order[random_order], dtype='float64')
    iranks = iseries.rank()
    tm.assert_series_equal(iranks, exp)