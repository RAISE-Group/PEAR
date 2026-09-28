def test_codes_dtypes(self):
    result = Categorical(['foo', 'bar', 'baz'])
    assert result.codes.dtype == 'int8'
    result = Categorical(['foo{i:05d}'.format(i=i) for i in range(400)])
    assert result.codes.dtype == 'int16'
    result = Categorical(['foo{i:05d}'.format(i=i) for i in range(40000)])
    assert result.codes.dtype == 'int32'
    result = Categorical(['foo', 'bar', 'baz'])
    assert result.codes.dtype == 'int8'
    result = result.add_categories(['foo{i:05d}'.format(i=i) for i in range(400)])
    assert result.codes.dtype == 'int16'
    result = result.remove_categories(['foo{i:05d}'.format(i=i) for i in range(300)])
    assert result.codes.dtype == 'int8'