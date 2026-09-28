@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
@pytest.mark.parametrize('file', ['dta14_113', 'dta14_114', 'dta14_115', 'dta14_117'])
def test_read_write_reread_dta14(self, file, parsed_114, version):
    file = getattr(self, file)
    parsed = self.read_dta(file)
    parsed.index.name = 'index'
    expected = self.read_csv(self.csv14)
    cols = ['byte_', 'int_', 'long_', 'float_', 'double_']
    for col in cols:
        expected[col] = expected[col]._convert(datetime=True, numeric=True)
    expected['float_'] = expected['float_'].astype(np.float32)
    expected['date_td'] = pd.to_datetime(expected['date_td'], errors='coerce')
    tm.assert_frame_equal(parsed_114, parsed)
    with tm.ensure_clean() as path:
        parsed_114.to_stata(path, {'date_td': 'td'}, version=version)
        written_and_read_again = self.read_dta(path)
        tm.assert_frame_equal(written_and_read_again.set_index('index'), parsed_114)