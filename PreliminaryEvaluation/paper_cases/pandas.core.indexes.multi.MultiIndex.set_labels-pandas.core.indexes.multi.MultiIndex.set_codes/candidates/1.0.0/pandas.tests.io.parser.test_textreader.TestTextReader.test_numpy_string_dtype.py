def test_numpy_string_dtype(self):
    data = 'a,1\naa,2\naaa,3\naaaa,4\naaaaa,5'

    def _make_reader(**kwds):
        return TextReader(StringIO(data), delimiter=',', header=None, **kwds)
    reader = _make_reader(dtype='S5,i4')
    result = reader.read()
    assert result[0].dtype == 'S5'
    ex_values = np.array(['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], dtype='S5')
    assert (result[0] == ex_values).all()
    assert result[1].dtype == 'i4'
    reader = _make_reader(dtype='S4')
    result = reader.read()
    assert result[0].dtype == 'S4'
    ex_values = np.array(['a', 'aa', 'aaa', 'aaaa', 'aaaa'], dtype='S4')
    assert (result[0] == ex_values).all()
    assert result[1].dtype == 'S4'