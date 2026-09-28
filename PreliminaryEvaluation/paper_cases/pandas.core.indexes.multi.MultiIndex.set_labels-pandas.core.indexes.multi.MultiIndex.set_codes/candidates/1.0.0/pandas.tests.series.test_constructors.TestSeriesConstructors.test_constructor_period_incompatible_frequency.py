def test_constructor_period_incompatible_frequency(self):
    data = [pd.Period('2000', 'D'), pd.Period('2001', 'A')]
    result = pd.Series(data)
    assert result.dtype == object
    assert result.tolist() == data