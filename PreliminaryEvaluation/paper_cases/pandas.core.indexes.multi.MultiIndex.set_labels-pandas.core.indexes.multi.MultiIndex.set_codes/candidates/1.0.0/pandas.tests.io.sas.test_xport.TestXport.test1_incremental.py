def test1_incremental(self):
    data_csv = pd.read_csv(self.file01.replace('.xpt', '.csv'))
    data_csv = data_csv.set_index('SEQN')
    numeric_as_float(data_csv)
    reader = read_sas(self.file01, index='SEQN', chunksize=1000)
    all_data = list(reader)
    data = pd.concat(all_data, axis=0)
    tm.assert_frame_equal(data, data_csv, check_index_type=False)