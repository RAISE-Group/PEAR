@pytest.mark.parametrize('empty,klass', [(PeriodIndex([], freq='B'), PeriodIndex), (PeriodIndex(iter([]), freq='B'), PeriodIndex), (PeriodIndex((_ for _ in []), freq='B'), PeriodIndex), (RangeIndex(step=1), pd.RangeIndex), (MultiIndex(levels=[[1, 2], ['blue', 'red']], codes=[[], []]), MultiIndex)])
def test_constructor_empty_special(self, empty, klass):
    assert isinstance(empty, klass)
    assert not len(empty)