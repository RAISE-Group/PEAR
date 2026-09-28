def test_to_csv_string_with_lf(self):
    data = {'int': [1, 2, 3], 'str_lf': ['abc', 'd\nef', 'g\nh\n\ni']}
    df = pd.DataFrame(data)
    with tm.ensure_clean('lf_test.csv') as path:
        os_linesep = os.linesep.encode('utf-8')
        expected_noarg = b'int,str_lf' + os_linesep + b'1,abc' + os_linesep + b'2,"d\nef"' + os_linesep + b'3,"g\nh\n\ni"' + os_linesep
        df.to_csv(path, index=False)
        with open(path, 'rb') as f:
            assert f.read() == expected_noarg
    with tm.ensure_clean('lf_test.csv') as path:
        expected_lf = b'int,str_lf\n1,abc\n2,"d\nef"\n3,"g\nh\n\ni"\n'
        df.to_csv(path, line_terminator='\n', index=False)
        with open(path, 'rb') as f:
            assert f.read() == expected_lf
    with tm.ensure_clean('lf_test.csv') as path:
        expected_crlf = b'int,str_lf\r\n1,abc\r\n2,"d\nef"\r\n3,"g\nh\n\ni"\r\n'
        df.to_csv(path, line_terminator='\r\n', index=False)
        with open(path, 'rb') as f:
            assert f.read() == expected_crlf