def test_constructor_no_pandas_array(self):
    ser = pd.Series([1, 2, 3])
    result = pd.Index(ser.array)
    expected = pd.Index([1, 2, 3])
    tm.assert_index_equal(result, expected)