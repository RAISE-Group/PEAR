def test_pandas_array_dtype(self, data):
    result = pd.array(data, dtype=np.dtype(object))
    expected = pd.arrays.PandasArray(np.asarray(data, dtype=object))
    self.assert_equal(result, expected)