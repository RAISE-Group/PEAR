def test_string_factorize(self):
    data = 'a\nb\na\nb\na'
    reader = TextReader(StringIO(data), header=None)
    result = reader.read()
    assert len(set(map(id, result[0]))) == 2