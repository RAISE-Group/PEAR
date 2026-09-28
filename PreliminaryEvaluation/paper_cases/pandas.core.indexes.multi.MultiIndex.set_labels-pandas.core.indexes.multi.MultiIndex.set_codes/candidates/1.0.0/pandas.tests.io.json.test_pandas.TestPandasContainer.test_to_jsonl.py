def test_to_jsonl(self):
    df = DataFrame([[1, 2], [1, 2]], columns=['a', 'b'])
    result = df.to_json(orient='records', lines=True)
    expected = '{"a":1,"b":2}\n{"a":1,"b":2}'
    assert result == expected
    df = DataFrame([['foo}', 'bar'], ['foo"', 'bar']], columns=['a', 'b'])
    result = df.to_json(orient='records', lines=True)
    expected = '{"a":"foo}","b":"bar"}\n{"a":"foo\\"","b":"bar"}'
    assert result == expected
    tm.assert_frame_equal(pd.read_json(result, lines=True), df)
    df = DataFrame([['foo\\', 'bar'], ['foo"', 'bar']], columns=['a\\', 'b'])
    result = df.to_json(orient='records', lines=True)
    expected = '{"a\\\\":"foo\\\\","b":"bar"}\n{"a\\\\":"foo\\"","b":"bar"}'
    assert result == expected
    tm.assert_frame_equal(pd.read_json(result, lines=True), df)