def test_constructor_empty(self):
    idx = pd.PeriodIndex([], freq='M')
    assert isinstance(idx, PeriodIndex)
    assert len(idx) == 0
    assert idx.freq == 'M'
    with pytest.raises(ValueError, match='freq not specified'):
        pd.PeriodIndex([])