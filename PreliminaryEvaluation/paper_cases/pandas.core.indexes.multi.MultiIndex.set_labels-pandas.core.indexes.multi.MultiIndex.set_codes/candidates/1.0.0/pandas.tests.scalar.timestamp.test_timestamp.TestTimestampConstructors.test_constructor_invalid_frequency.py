def test_constructor_invalid_frequency(self):
    with pytest.raises(ValueError, match='Invalid frequency:'):
        Timestamp('2012-01-01', freq=[])