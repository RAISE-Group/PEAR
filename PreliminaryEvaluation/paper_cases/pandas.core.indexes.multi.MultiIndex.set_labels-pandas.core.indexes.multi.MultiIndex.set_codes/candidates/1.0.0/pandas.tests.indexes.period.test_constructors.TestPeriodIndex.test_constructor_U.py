def test_constructor_U(self):
    with pytest.raises(ValueError, match='Invalid frequency: X'):
        period_range('2007-1-1', periods=500, freq='X')