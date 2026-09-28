def test_csv_to_string(self):
    df = DataFrame({'col': [1, 2]})
    expected_rows = [',col', '0,1', '1,2']
    expected = tm.convert_rows_list_to_csv_str(expected_rows)
    assert df.to_csv() == expected