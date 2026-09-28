def test_parse_booleans(self):
    data = 'True\nFalse\nTrue\nTrue'
    reader = TextReader(StringIO(data), header=None)
    result = reader.read()
    assert result[0].dtype == np.bool_