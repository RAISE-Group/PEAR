def test_append_missing_cols(self):
    df = DataFrame(np.random.randn(5, 4), columns=['foo', 'bar', 'baz', 'qux'])
    dicts = [{'foo': 9}, {'bar': 10}]
    with tm.assert_produces_warning(None):
        result = df.append(dicts, ignore_index=True, sort=True)
    expected = df.append(DataFrame(dicts), ignore_index=True, sort=True)
    tm.assert_frame_equal(result, expected)