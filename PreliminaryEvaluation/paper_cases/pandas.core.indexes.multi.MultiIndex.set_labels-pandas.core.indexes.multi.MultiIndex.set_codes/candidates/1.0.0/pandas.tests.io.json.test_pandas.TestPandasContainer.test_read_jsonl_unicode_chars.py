def test_read_jsonl_unicode_chars(self):
    json = '{"a": "foo”", "b": "bar"}\n{"a": "foo", "b": "bar"}\n'
    json = StringIO(json)
    result = read_json(json, lines=True)
    expected = DataFrame([['foo”', 'bar'], ['foo', 'bar']], columns=['a', 'b'])
    tm.assert_frame_equal(result, expected)
    json = '{"a": "foo”", "b": "bar"}\n{"a": "foo", "b": "bar"}\n'
    result = read_json(json, lines=True)
    expected = DataFrame([['foo”', 'bar'], ['foo', 'bar']], columns=['a', 'b'])
    tm.assert_frame_equal(result, expected)