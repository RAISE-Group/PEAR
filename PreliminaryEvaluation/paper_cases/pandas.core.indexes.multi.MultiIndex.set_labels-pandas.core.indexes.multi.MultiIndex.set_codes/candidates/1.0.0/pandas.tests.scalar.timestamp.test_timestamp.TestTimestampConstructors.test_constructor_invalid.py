def test_constructor_invalid(self):
    with pytest.raises(TypeError, match='Cannot convert input'):
        Timestamp(slice(2))
    with pytest.raises(ValueError, match='Cannot convert Period'):
        Timestamp(Period('1000-01-01'))