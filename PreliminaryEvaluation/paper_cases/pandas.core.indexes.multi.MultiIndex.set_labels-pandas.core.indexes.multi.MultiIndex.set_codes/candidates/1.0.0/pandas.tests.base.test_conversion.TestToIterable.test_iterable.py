@pytest.mark.parametrize('dtype, rdtype', dtypes)
@pytest.mark.parametrize('method', [lambda x: x.tolist(), lambda x: x.to_list(), lambda x: list(x), lambda x: list(x.__iter__())], ids=['tolist', 'to_list', 'list', 'iter'])
@pytest.mark.filterwarnings('ignore:\\n    Passing:FutureWarning')
def test_iterable(self, index_or_series, method, dtype, rdtype):
    typ = index_or_series
    s = typ([1], dtype=dtype)
    result = method(s)[0]
    assert isinstance(result, rdtype)