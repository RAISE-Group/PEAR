@pytest.mark.xfail(compat.is_platform_windows(), reason="Especially in Windows, file stream should not be passedto csv writer without newline='' option.(https://docs.python.org/3.6/library/csv.html#csv.writer)")
def test_to_csv_write_to_open_file(self):
    df = pd.DataFrame({'a': ['x', 'y', 'z']})
    expected = 'manual header\nx\ny\nz\n'
    with tm.ensure_clean('test.txt') as path:
        with open(path, 'w') as f:
            f.write('manual header\n')
            df.to_csv(f, header=None, index=None)
        with open(path, 'r') as f:
            assert f.read() == expected