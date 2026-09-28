def test1_basic(self):
    data_csv = pd.read_csv(self.file01.replace('.xpt', '.csv'))
    numeric_as_float(data_csv)
    data = read_sas(self.file01, format='xport')
    tm.assert_frame_equal(data, data_csv)
    num_rows = data.shape[0]
    reader = read_sas(self.file01, format='xport', iterator=True)
    data = reader.read(num_rows + 100)
    assert data.shape[0] == num_rows
    reader.close()
    reader = read_sas(self.file01, format='xport', iterator=True)
    data = reader.read(10)
    reader.close()
    tm.assert_frame_equal(data, data_csv.iloc[0:10, :])
    reader = read_sas(self.file01, format='xport', chunksize=10)
    data = reader.get_chunk()
    reader.close()
    tm.assert_frame_equal(data, data_csv.iloc[0:10, :])
    m = 0
    reader = read_sas(self.file01, format='xport', chunksize=100)
    for x in reader:
        m += x.shape[0]
    reader.close()
    assert m == num_rows
    data = read_sas(self.file01)
    tm.assert_frame_equal(data, data_csv)