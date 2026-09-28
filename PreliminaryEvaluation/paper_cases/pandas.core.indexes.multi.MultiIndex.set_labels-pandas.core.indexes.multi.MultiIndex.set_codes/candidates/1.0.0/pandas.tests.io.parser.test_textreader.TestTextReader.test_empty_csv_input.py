def test_empty_csv_input(self):
    df = read_csv(StringIO(), chunksize=20, header=None, names=['a', 'b', 'c'])
    assert isinstance(df, TextFileReader)