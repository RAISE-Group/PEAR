def test_append_list_of_series_dicts(self):
    df = DataFrame(np.random.randn(5, 4), columns=['foo', 'bar', 'baz', 'qux'])
    dicts = [x.to_dict() for idx, x in df.iterrows()]
    result = df.append(dicts, ignore_index=True)
    expected = df.append(df, ignore_index=True)
    tm.assert_frame_equal(result, expected)
    dicts = [{'foo': 1, 'bar': 2, 'baz': 3, 'peekaboo': 4}, {'foo': 5, 'bar': 6, 'baz': 7, 'peekaboo': 8}]
    result = df.append(dicts, ignore_index=True, sort=True)
    expected = df.append(DataFrame(dicts), ignore_index=True, sort=True)
    tm.assert_frame_equal(result, expected)