def test_reading_all_sheets(self, read_ext):
    basename = 'test_multisheet'
    dfs = pd.read_excel(basename + read_ext, sheet_name=None)
    expected_keys = ['Charlie', 'Alpha', 'Beta']
    tm.assert_contains_all(expected_keys, dfs.keys())
    assert expected_keys == list(dfs.keys())