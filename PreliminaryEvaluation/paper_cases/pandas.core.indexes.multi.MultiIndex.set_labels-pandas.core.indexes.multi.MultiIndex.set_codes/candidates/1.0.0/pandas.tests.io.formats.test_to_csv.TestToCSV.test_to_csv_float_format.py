def test_to_csv_float_format(self):
    df = pd.DataFrame({'a': [0, 1], 'b': [2.2, 3.3], 'c': 1})
    expected_rows = ['a,b,c', '0,2.20,1', '1,3.30,1']
    expected = tm.convert_rows_list_to_csv_str(expected_rows)
    assert df.set_index('a').to_csv(float_format='%.2f') == expected
    assert df.set_index(['a', 'b']).to_csv(float_format='%.2f') == expected