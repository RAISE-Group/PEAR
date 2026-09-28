def test_usecols(self):
    data = 'a,b,c\n1,2,3\n4,5,6\n7,8,9\n10,11,12'

    def _make_reader(**kwds):
        return TextReader(StringIO(data), delimiter=',', **kwds)
    reader = _make_reader(usecols=(1, 2))
    result = reader.read()
    exp = _make_reader().read()
    assert len(result) == 2
    assert (result[1] == exp[1]).all()
    assert (result[2] == exp[2]).all()