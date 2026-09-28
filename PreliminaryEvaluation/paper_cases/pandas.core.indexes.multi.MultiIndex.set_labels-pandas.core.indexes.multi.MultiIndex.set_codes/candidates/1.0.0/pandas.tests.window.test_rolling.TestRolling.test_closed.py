def test_closed(self):
    df = DataFrame({'A': [0, 1, 2, 3, 4]})
    with pytest.raises(ValueError):
        df.rolling(window=3, closed='neither')