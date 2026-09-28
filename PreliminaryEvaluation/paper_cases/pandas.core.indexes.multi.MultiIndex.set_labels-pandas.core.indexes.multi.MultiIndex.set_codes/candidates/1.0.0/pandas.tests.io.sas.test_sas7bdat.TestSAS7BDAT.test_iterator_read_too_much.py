def test_iterator_read_too_much(self):
    k = self.test_ix[0][0]
    fname = os.path.join(self.dirpath, f'test{k}.sas7bdat')
    rdr = pd.read_sas(fname, format='sas7bdat', iterator=True, encoding='utf-8')
    d1 = rdr.read(rdr.row_count + 20)
    rdr.close()
    rdr = pd.read_sas(fname, iterator=True, encoding='utf-8')
    d2 = rdr.read(rdr.row_count + 20)
    tm.assert_frame_equal(d1, d2)
    rdr.close()