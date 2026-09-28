def test_truncated_float_support(self):
    data_csv = pd.read_csv(self.file04.replace('.xpt', '.csv'))
    data = read_sas(self.file04, format='xport')
    tm.assert_frame_equal(data.astype('int64'), data_csv)