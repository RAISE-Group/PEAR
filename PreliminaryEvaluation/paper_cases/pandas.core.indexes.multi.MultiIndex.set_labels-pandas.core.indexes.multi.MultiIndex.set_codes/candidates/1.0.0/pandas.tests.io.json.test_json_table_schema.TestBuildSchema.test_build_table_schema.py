def test_build_table_schema(self):
    result = build_table_schema(self.df, version=False)
    expected = {'fields': [{'name': 'idx', 'type': 'integer'}, {'name': 'A', 'type': 'integer'}, {'name': 'B', 'type': 'string'}, {'name': 'C', 'type': 'datetime'}, {'name': 'D', 'type': 'duration'}], 'primaryKey': ['idx']}
    assert result == expected
    result = build_table_schema(self.df)
    assert 'pandas_version' in result