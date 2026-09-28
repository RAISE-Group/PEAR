def test_from_file(self):
    for j in (0, 1):
        df0 = self.data[j]
        for k in self.test_ix[j]:
            fname = os.path.join(self.dirpath, f'test{k}.sas7bdat')
            df = pd.read_sas(fname, encoding='utf-8')
            tm.assert_frame_equal(df, df0)