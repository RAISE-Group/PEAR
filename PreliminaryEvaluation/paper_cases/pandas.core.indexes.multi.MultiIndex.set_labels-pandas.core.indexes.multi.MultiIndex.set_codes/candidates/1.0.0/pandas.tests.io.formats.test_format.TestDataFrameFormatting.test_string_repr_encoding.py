def test_string_repr_encoding(self, datapath):
    filepath = datapath('io', 'parser', 'data', 'unicode_series.csv')
    df = pd.read_csv(filepath, header=None, encoding='latin1')
    repr(df)
    repr(df[1])