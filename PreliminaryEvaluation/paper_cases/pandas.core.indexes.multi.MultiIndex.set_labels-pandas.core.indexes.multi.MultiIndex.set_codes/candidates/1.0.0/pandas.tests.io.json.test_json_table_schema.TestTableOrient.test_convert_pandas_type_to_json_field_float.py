def test_convert_pandas_type_to_json_field_float(self, index_or_series):
    kind = index_or_series
    data = [1.0, 2.0, 3.0]
    result = convert_pandas_type_to_json_field(kind(data, name='name'))
    expected = {'name': 'name', 'type': 'number'}
    assert result == expected