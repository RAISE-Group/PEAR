def test_to_csv_interval_index(self):
    df = DataFrame({'A': list('abc'), 'B': range(3)}, index=pd.interval_range(0, 3))
    with tm.ensure_clean('__tmp_to_csv_interval_index__.csv') as path:
        df.to_csv(path)
        result = self.read_csv(path, index_col=0)
        expected = df.copy()
        expected.index = expected.index.astype(str)
        tm.assert_frame_equal(result, expected)