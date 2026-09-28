def test_multiple_types(self):
    data_csv = pd.read_csv(self.file03.replace('.xpt', '.csv'))
    data = read_sas(self.file03, encoding='utf-8')
    tm.assert_frame_equal(data, data_csv)