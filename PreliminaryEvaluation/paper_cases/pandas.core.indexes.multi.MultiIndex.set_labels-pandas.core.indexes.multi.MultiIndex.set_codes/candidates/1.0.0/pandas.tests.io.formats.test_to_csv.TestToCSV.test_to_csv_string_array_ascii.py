def test_to_csv_string_array_ascii(self):
    str_array = [{'names': ['foo', 'bar']}, {'names': ['baz', 'qux']}]
    df = pd.DataFrame(str_array)
    expected_ascii = ',names\n0,"[\'foo\', \'bar\']"\n1,"[\'baz\', \'qux\']"\n'
    with tm.ensure_clean('str_test.csv') as path:
        df.to_csv(path, encoding='ascii')
        with open(path, 'r') as f:
            assert f.read() == expected_ascii