def test_invalid_kind(self):
    df = DataFrame(randn(10, 2))
    with pytest.raises(ValueError):
        df.plot(kind='aasdf')