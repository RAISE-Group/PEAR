def test_to_csv_string_array_utf8(self):
    str_array = [{'names': ['foo', 'bar']}, {'names': ['baz', 'qux']}]
    df = pd.DataFrame(str_array)
    expected_utf8 = ',names\n0,"[\'foo\', \'bar\']"\n1,"[\'baz\', \'qux\']"\n'
    with tm.ensure_clean('unicode_test.csv') as path:
        df.to_csv(path, encoding='utf-8')
        with open(path, 'r') as f:
            assert f.read() == expected_utf8