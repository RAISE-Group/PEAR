def test_gz_lineend(self):
    df = pd.DataFrame({'a': [1, 2]})
    expected_rows = ['a', '1', '2']
    expected = tm.convert_rows_list_to_csv_str(expected_rows)
    with tm.ensure_clean('__test_gz_lineend.csv.gz') as path:
        df.to_csv(path, index=False)
        with tm.decompress_file(path, compression='gzip') as f:
            result = f.read().decode('utf-8')
    assert result == expected