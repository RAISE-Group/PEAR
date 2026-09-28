def test_get_numeric_data_preserve_dtype(self):
    o = DataFrame({'A': [1, '2', 3.0]})
    result = o._get_numeric_data()
    expected = DataFrame(index=[0, 1, 2], dtype=object)
    self._compare(result, expected)