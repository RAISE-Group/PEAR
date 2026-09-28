def test_constructor_no_pandas_array(self):
    ser = pd.Series([1, 2, 3])
    result = pd.Series(ser.array)
    tm.assert_series_equal(ser, result)
    assert isinstance(result._data.blocks[0], IntBlock)