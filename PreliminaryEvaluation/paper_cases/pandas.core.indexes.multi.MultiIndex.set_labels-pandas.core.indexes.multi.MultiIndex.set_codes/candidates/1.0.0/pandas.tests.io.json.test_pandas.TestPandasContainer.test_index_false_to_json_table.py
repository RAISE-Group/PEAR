@pytest.mark.parametrize('data', [DataFrame([[1, 2], [4, 5]], columns=['a', 'b']), DataFrame([[1, 2], [4, 5]], columns=['a', 'b']).rename_axis('foo'), DataFrame([[1, 2], [4, 5]], columns=['a', 'b'], index=[['a', 'b'], ['c', 'd']]), Series([1, 2, 3], name='A'), Series([1, 2, 3], name='A').rename_axis('foo'), Series([1, 2], name='A', index=[['a', 'b'], ['c', 'd']])])
def test_index_false_to_json_table(self, data):
    result = data.to_json(orient='table', index=False)
    result = json.loads(result)
    expected = {'schema': pd.io.json.build_table_schema(data, index=False), 'data': DataFrame(data).to_dict(orient='records')}
    assert result == expected