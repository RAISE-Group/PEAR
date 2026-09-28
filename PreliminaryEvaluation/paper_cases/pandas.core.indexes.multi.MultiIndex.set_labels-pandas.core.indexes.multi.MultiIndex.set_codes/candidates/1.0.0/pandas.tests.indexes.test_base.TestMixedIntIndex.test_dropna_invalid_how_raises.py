def test_dropna_invalid_how_raises(self):
    msg = 'invalid how option: xxx'
    with pytest.raises(ValueError, match=msg):
        pd.Index([1, 2, 3]).dropna(how='xxx')