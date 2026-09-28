def test_invalid_encoding(self, df):
    with pytest.raises(ValueError):
        df.to_clipboard(encoding='ascii')
    with pytest.raises(NotImplementedError):
        pd.read_clipboard(encoding='ascii')