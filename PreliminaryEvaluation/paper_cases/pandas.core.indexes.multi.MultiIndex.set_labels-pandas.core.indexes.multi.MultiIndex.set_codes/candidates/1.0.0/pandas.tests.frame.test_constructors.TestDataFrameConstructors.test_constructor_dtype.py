@pytest.mark.parametrize('data, index, columns, dtype, expected', [(None, list(range(10)), ['a', 'b'], object, np.object_), (None, None, ['a', 'b'], 'int64', np.dtype('int64')), (None, list(range(10)), ['a', 'b'], int, np.dtype('float64')), ({}, None, ['foo', 'bar'], None, np.object_), ({'b': 1}, list(range(10)), list('abc'), int, np.dtype('float64'))])
def test_constructor_dtype(self, data, index, columns, dtype, expected):
    df = DataFrame(data, index, columns, dtype)
    assert df.values.dtype == expected