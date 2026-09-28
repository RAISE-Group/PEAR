def test_apply_empty_infer_type(self):
    no_cols = DataFrame(index=['a', 'b', 'c'])
    no_index = DataFrame(columns=['a', 'b', 'c'])

    def _check(df, f):
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('ignore', RuntimeWarning)
            test_res = f(np.array([], dtype='f8'))
        is_reduction = not isinstance(test_res, np.ndarray)

        def _checkit(axis=0, raw=False):
            result = df.apply(f, axis=axis, raw=raw)
            if is_reduction:
                agg_axis = df._get_agg_axis(axis)
                assert isinstance(result, Series)
                assert result.index is agg_axis
            else:
                assert isinstance(result, DataFrame)
        _checkit()
        _checkit(axis=1)
        _checkit(raw=True)
        _checkit(axis=0, raw=True)
    with np.errstate(all='ignore'):
        _check(no_cols, lambda x: x)
        _check(no_cols, lambda x: x.mean())
        _check(no_index, lambda x: x)
        _check(no_index, lambda x: x.mean())
    result = no_cols.apply(lambda x: x.mean(), result_type='broadcast')
    assert isinstance(result, DataFrame)