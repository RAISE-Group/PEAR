def test_constructor_list_of_lists(self):
    df = DataFrame(data=[[1, 'a'], [2, 'b']], columns=['num', 'str'])
    assert is_integer_dtype(df['num'])
    assert df['str'].dtype == np.object_
    expected = DataFrame({0: np.arange(10)})
    data = [np.array(x) for x in range(10)]
    result = DataFrame(data)
    tm.assert_frame_equal(result, expected)