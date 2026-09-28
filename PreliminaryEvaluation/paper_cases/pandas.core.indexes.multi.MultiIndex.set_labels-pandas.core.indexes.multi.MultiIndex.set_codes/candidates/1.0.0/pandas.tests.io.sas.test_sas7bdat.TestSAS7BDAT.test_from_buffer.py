def test_from_buffer(self):
    for j in (0, 1):
        df0 = self.data[j]
        for k in self.test_ix[j]:
            fname = os.path.join(self.dirpath, f'test{k}.sas7bdat')
            with open(fname, 'rb') as f:
                byts = f.read()
            buf = io.BytesIO(byts)
            rdr = pd.read_sas(buf, format='sas7bdat', iterator=True, encoding='utf-8')
            df = rdr.read()
            tm.assert_frame_equal(df, df0, check_exact=False)
            rdr.close()