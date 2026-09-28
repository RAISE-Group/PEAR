@pytest.mark.slow
def test_stata_119(self):
    with gzip.open(self.dta26_119, 'rb') as gz:
        df = read_stata(gz)
    assert df.shape == (1, 32999)
    assert df.iloc[0, 6] == 'A' * 3000
    assert df.iloc[0, 7] == 3.14
    assert df.iloc[0, -1] == 1
    assert df.iloc[0, 0] == pd.Timestamp(datetime(2012, 12, 21, 21, 12, 21))