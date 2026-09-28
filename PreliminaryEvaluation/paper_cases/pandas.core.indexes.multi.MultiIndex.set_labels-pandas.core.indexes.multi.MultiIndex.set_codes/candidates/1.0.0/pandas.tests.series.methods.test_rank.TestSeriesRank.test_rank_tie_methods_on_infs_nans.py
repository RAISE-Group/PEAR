@td.skip_if_no_scipy
@pytest.mark.parametrize('ascending', [True, False])
@pytest.mark.parametrize('method', ['average', 'min', 'max', 'first', 'dense'])
@pytest.mark.parametrize('na_option', ['top', 'bottom', 'keep'])
def test_rank_tie_methods_on_infs_nans(self, method, na_option, ascending):
    dtypes = [('object', None, Infinity(), NegInfinity()), ('float64', np.nan, np.inf, -np.inf)]
    chunk = 3
    disabled = {('object', 'first')}

    def _check(s, method, na_option, ascending):
        exp_ranks = {'average': ([2, 2, 2], [5, 5, 5], [8, 8, 8]), 'min': ([1, 1, 1], [4, 4, 4], [7, 7, 7]), 'max': ([3, 3, 3], [6, 6, 6], [9, 9, 9]), 'first': ([1, 2, 3], [4, 5, 6], [7, 8, 9]), 'dense': ([1, 1, 1], [2, 2, 2], [3, 3, 3])}
        ranks = exp_ranks[method]
        if na_option == 'top':
            order = [ranks[1], ranks[0], ranks[2]]
        elif na_option == 'bottom':
            order = [ranks[0], ranks[2], ranks[1]]
        else:
            order = [ranks[0], [np.nan] * chunk, ranks[1]]
        expected = order if ascending else order[::-1]
        expected = list(chain.from_iterable(expected))
        result = s.rank(method=method, na_option=na_option, ascending=ascending)
        tm.assert_series_equal(result, Series(expected, dtype='float64'))
    for dtype, na_value, pos_inf, neg_inf in dtypes:
        in_arr = [neg_inf] * chunk + [na_value] * chunk + [pos_inf] * chunk
        iseries = Series(in_arr, dtype=dtype)
        if (dtype, method) in disabled:
            continue
        _check(iseries, method, na_option, ascending)