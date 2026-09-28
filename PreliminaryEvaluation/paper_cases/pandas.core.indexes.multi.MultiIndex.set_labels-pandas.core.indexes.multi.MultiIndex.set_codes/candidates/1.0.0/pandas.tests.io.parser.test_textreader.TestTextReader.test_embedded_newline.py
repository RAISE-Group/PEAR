def test_embedded_newline(self):
    data = 'a\n"hello\nthere"\nthis'
    reader = TextReader(StringIO(data), header=None)
    result = reader.read()
    expected = np.array(['a', 'hello\nthere', 'this'], dtype=np.object_)
    tm.assert_numpy_array_equal(result[0], expected)