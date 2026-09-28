def test_euro_decimal(self):
    data = '12345,67\n345,678'
    reader = TextReader(StringIO(data), delimiter=':', decimal=',', header=None)
    result = reader.read()
    expected = np.array([12345.67, 345.678])
    tm.assert_almost_equal(result[0], expected)