def test_append_empty_list(self):
    df = DataFrame()
    result = df.append([])
    expected = df
    tm.assert_frame_equal(result, expected)
    assert result is not df
    df = DataFrame(np.random.randn(5, 4), columns=['foo', 'bar', 'baz', 'qux'])
    result = df.append([])
    expected = df
    tm.assert_frame_equal(result, expected)
    assert result is not df