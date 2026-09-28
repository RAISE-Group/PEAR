def test_integer_thousands(self):
    data = '123,456\n12,500'
    reader = TextReader(StringIO(data), delimiter=':', thousands=',', header=None)
    result = reader.read()
    expected = np.array([123456, 12500], dtype=np.int64)
    tm.assert_almost_equal(result[0], expected)