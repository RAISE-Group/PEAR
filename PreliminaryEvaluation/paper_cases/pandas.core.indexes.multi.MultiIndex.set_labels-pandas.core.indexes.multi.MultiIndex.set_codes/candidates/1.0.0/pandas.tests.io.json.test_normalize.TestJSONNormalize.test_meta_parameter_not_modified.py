def test_meta_parameter_not_modified(self):
    data = [{'foo': 'hello', 'bar': 'there', 'data': [{'foo': 'something', 'bar': 'else'}, {'foo': 'something2', 'bar': 'else2'}]}]
    COLUMNS = ['foo', 'bar']
    result = json_normalize(data, 'data', meta=COLUMNS, meta_prefix='meta')
    assert COLUMNS == ['foo', 'bar']
    for val in ['metafoo', 'metabar', 'foo', 'bar']:
        assert val in result