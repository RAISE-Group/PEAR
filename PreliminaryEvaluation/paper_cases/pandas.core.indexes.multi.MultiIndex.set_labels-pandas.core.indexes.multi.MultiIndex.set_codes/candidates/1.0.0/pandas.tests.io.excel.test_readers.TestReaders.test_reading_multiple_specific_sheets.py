def test_reading_multiple_specific_sheets(self, read_ext):
    basename = 'test_multisheet'
    expected_keys = [2, 'Charlie', 'Charlie']
    dfs = pd.read_excel(basename + read_ext, sheet_name=expected_keys)
    expected_keys = list(set(expected_keys))
    tm.assert_contains_all(expected_keys, dfs.keys())
    assert len(expected_keys) == len(dfs.keys())