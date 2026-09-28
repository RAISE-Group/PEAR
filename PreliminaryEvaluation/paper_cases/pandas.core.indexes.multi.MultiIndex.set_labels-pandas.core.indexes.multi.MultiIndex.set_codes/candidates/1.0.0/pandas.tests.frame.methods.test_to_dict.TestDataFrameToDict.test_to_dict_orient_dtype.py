def test_to_dict_orient_dtype(self):
    input_data = {'a': [1, 2, 3], 'b': [1.0, 2.0, 3.0], 'c': ['X', 'Y', 'Z']}
    df = DataFrame(input_data)
    expected = {'a': int, 'b': float, 'c': str}
    for df_dict in df.to_dict('records'):
        result = {'a': type(df_dict['a']), 'b': type(df_dict['b']), 'c': type(df_dict['c'])}
        assert result == expected