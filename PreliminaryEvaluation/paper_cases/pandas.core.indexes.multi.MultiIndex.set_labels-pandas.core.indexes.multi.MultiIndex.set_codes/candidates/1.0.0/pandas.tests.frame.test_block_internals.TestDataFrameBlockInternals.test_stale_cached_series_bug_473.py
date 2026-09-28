def test_stale_cached_series_bug_473(self):
    with option_context('chained_assignment', None):
        Y = DataFrame(np.random.random((4, 4)), index=('a', 'b', 'c', 'd'), columns=('e', 'f', 'g', 'h'))
        repr(Y)
        Y['e'] = Y['e'].astype('object')
        Y['g']['c'] = np.NaN
        repr(Y)
        result = Y.sum()
        exp = Y['g'].sum()
        assert pd.isna(Y['g']['c'])