@pytest.mark.xfail((3, 6, 5) > sys.version_info, reason='Python csv library bug (see https://bugs.python.org/issue32255)')
def test_to_csv_with_single_column(self):
    df1 = DataFrame([None, 1])
    expected1 = '""\n1.0\n'
    with tm.ensure_clean('test.csv') as path:
        df1.to_csv(path, header=None, index=None)
        with open(path, 'r') as f:
            assert f.read() == expected1
    df2 = DataFrame([1, None])
    expected2 = '1.0\n""\n'
    with tm.ensure_clean('test.csv') as path:
        df2.to_csv(path, header=None, index=None)
        with open(path, 'r') as f:
            assert f.read() == expected2