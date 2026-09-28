def test_constructor_no_pandas_array(self):
    arr = pd.Series([1, 2, 3]).array
    result = pd.DataFrame({'A': arr})
    expected = pd.DataFrame({'A': [1, 2, 3]})
    tm.assert_frame_equal(result, expected)
    assert isinstance(result._data.blocks[0], IntBlock)