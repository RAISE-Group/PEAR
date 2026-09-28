def test_invalid_arguments(self):
    with pytest.raises(ValueError):
        Period(datetime.now())
    with pytest.raises(ValueError):
        Period(datetime.now().date())
    with pytest.raises(ValueError):
        Period(1.6, freq='D')
    with pytest.raises(ValueError):
        Period(ordinal=1.6, freq='D')
    with pytest.raises(ValueError):
        Period(ordinal=2, value=1, freq='D')
    with pytest.raises(ValueError):
        Period(month=1)
    with pytest.raises(ValueError):
        Period('-2000', 'A')
    with pytest.raises(DateParseError):
        Period('0', 'A')
    with pytest.raises(DateParseError):
        Period('1/1/-2000', 'A')