@pytest.mark.parametrize('dtype, rdtype, obj', [('object', object, 'a'), ('object', int, 1), ('category', object, 'a'), ('category', int, 1)])
@pytest.mark.parametrize('method', [lambda x: x.tolist(), lambda x: x.to_list(), lambda x: list(x), lambda x: list(x.__iter__())], ids=['tolist', 'to_list', 'list', 'iter'])
def test_iterable_object_and_category(self, index_or_series, method, dtype, rdtype, obj):
    typ = index_or_series
    s = typ([obj], dtype=dtype)
    result = method(s)[0]
    assert isinstance(result, rdtype)