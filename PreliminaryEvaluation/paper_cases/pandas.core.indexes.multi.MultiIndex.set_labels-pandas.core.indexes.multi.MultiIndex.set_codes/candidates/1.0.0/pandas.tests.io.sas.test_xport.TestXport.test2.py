def test2(self):
    data_csv = pd.read_csv(self.file02.replace('.xpt', '.csv'))
    numeric_as_float(data_csv)
    data = read_sas(self.file02)
    tm.assert_frame_equal(data, data_csv)