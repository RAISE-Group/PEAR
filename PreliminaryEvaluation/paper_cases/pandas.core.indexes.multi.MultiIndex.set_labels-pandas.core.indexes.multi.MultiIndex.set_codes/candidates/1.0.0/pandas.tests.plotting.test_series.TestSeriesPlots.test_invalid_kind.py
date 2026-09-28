def test_invalid_kind(self):
    s = Series([1, 2])
    with pytest.raises(ValueError):
        s.plot(kind='aasdf')