def test_convert_pandas_type_to_json_period_range(self):
    arr = pd.period_range('2016', freq='A-DEC', periods=4)
    result = convert_pandas_type_to_json_field(arr)
    expected = {'name': 'values', 'type': 'datetime', 'freq': 'A-DEC'}
    assert result == expected