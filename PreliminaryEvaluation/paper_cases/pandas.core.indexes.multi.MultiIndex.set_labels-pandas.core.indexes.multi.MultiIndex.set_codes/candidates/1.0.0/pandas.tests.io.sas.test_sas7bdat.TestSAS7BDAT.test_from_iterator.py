def test_from_iterator(self):
    for j in (0, 1):
        df0 = self.data[j]
        for k in self.test_ix[j]:
            fname = os.path.join(self.dirpath, f'test{k}.sas7bdat')
            rdr = pd.read_sas(fname, iterator=True, encoding='utf-8')
            df = rdr.read(2)
            tm.assert_frame_equal(df, df0.iloc[0:2, :])
            df = rdr.read(3)
            tm.assert_frame_equal(df, df0.iloc[2:5, :])
            rdr.close()