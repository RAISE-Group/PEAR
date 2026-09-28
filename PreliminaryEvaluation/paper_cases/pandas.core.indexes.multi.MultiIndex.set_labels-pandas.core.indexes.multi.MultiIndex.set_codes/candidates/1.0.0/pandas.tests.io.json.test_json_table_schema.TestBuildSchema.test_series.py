def test_series(self):
    s = pd.Series([1, 2, 3], name='foo')
    result = build_table_schema(s, version=False)
    expected = {'fields': [{'name': 'index', 'type': 'integer'}, {'name': 'foo', 'type': 'integer'}], 'primaryKey': ['index']}
    assert result == expected
    result = build_table_schema(s)
    assert 'pandas_version' in result