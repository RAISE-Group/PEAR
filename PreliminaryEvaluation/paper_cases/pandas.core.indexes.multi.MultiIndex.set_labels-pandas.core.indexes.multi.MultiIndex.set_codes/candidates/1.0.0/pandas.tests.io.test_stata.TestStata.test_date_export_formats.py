def test_date_export_formats(self):
    columns = ['tc', 'td', 'tw', 'tm', 'tq', 'th', 'ty']
    conversions = {c: c for c in columns}
    data = [datetime(2006, 11, 20, 23, 13, 20)] * len(columns)
    original = DataFrame([data], columns=columns)
    original.index.name = 'index'
    expected_values = [datetime(2006, 11, 20, 23, 13, 20), datetime(2006, 11, 20), datetime(2006, 11, 19), datetime(2006, 11, 1), datetime(2006, 10, 1), datetime(2006, 7, 1), datetime(2006, 1, 1)]
    expected = DataFrame([expected_values], columns=columns)
    expected.index.name = 'index'
    with tm.ensure_clean() as path:
        original.to_stata(path, conversions)
        written_and_read_again = self.read_dta(path)
        tm.assert_frame_equal(written_and_read_again.set_index('index'), expected)