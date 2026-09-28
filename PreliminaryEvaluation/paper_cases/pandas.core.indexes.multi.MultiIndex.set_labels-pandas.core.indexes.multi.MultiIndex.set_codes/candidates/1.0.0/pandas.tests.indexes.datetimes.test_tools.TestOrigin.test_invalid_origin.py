def test_invalid_origin(self):
    with pytest.raises(ValueError):
        pd.to_datetime('2005-01-01', origin='1960-01-01')
    with pytest.raises(ValueError):
        pd.to_datetime('2005-01-01', origin='1960-01-01', unit='D')