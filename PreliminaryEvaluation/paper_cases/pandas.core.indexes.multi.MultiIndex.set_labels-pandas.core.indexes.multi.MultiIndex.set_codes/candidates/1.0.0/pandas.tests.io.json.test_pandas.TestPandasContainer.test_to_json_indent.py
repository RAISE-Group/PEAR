@pytest.mark.parametrize('indent', [1, 2, 4])
def test_to_json_indent(self, indent):
    df = pd.DataFrame([['foo', 'bar'], ['baz', 'qux']], columns=['a', 'b'])
    result = df.to_json(indent=indent)
    spaces = ' ' * indent
    expected = f'{{\n{spaces}"a":{{\n{spaces}{spaces}"0":"foo",\n{spaces}{spaces}"1":"baz"\n{spaces}}},\n{spaces}"b":{{\n{spaces}{spaces}"0":"bar",\n{spaces}{spaces}"1":"qux"\n{spaces}}}\n}}'
    assert result == expected