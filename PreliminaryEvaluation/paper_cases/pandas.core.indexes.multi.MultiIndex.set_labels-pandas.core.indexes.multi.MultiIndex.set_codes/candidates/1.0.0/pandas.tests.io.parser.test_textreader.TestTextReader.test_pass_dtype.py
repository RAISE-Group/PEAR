def test_pass_dtype(self):
    data = 'one,two\n1,a\n2,b\n3,c\n4,d'

    def _make_reader(**kwds):
        return TextReader(StringIO(data), delimiter=',', **kwds)
    reader = _make_reader(dtype={'one': 'u1', 1: 'S1'})
    result = reader.read()
    assert result[0].dtype == 'u1'
    assert result[1].dtype == 'S1'
    reader = _make_reader(dtype={'one': np.uint8, 1: object})
    result = reader.read()
    assert result[0].dtype == 'u1'
    assert result[1].dtype == 'O'
    reader = _make_reader(dtype={'one': np.dtype('u1'), 1: np.dtype('O')})
    result = reader.read()
    assert result[0].dtype == 'u1'
    assert result[1].dtype == 'O'