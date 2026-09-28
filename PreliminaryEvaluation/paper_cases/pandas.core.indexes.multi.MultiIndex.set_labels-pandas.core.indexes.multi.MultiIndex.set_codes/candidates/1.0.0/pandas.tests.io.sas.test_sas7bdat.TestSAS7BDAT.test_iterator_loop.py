def test_iterator_loop(self):
    for j in (0, 1):
        for k in self.test_ix[j]:
            for chunksize in (3, 5, 10, 11):
                fname = os.path.join(self.dirpath, f'test{k}.sas7bdat')
                rdr = pd.read_sas(fname, chunksize=10, encoding='utf-8')
                y = 0
                for x in rdr:
                    y += x.shape[0]
                assert y == rdr.row_count
                rdr.close()