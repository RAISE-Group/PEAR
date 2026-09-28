@pytest.mark.parametrize('func', [np.any, np.all])
@pytest.mark.parametrize('kwargs', [dict(keepdims=True), dict(out=object())])
@td.skip_if_np_lt('1.15')
def test_validate_any_all_out_keepdims_raises(self, kwargs, func):
    s = pd.Series([1, 2])
    param = list(kwargs)[0]
    name = func.__name__
    msg = "the '{arg}' parameter is not supported in the pandas implementation of {fname}\\(\\)".format(arg=param, fname=name)
    with pytest.raises(ValueError, match=msg):
        func(s, **kwargs)