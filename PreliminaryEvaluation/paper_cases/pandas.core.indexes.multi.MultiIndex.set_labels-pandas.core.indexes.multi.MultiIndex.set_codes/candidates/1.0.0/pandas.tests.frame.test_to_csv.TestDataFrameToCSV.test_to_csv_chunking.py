def test_to_csv_chunking(self):
    aa = DataFrame({'A': range(100000)})
    aa['B'] = aa.A + 1.0
    aa['C'] = aa.A + 2.0
    aa['D'] = aa.A + 3.0
    for chunksize in [10000, 50000, 100000]:
        with tm.ensure_clean() as filename:
            aa.to_csv(filename, chunksize=chunksize)
            rs = read_csv(filename, index_col=0)
            tm.assert_frame_equal(rs, aa)