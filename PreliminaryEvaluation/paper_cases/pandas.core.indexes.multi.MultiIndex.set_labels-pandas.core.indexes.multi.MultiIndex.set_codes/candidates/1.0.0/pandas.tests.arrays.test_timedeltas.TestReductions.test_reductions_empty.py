@pytest.mark.parametrize('name', ['sum', 'std', 'min', 'max', 'median'])
@pytest.mark.parametrize('skipna', [True, False])
def test_reductions_empty(self, name, skipna):
    tdi = pd.TimedeltaIndex([])
    arr = tdi.array
    result = getattr(tdi, name)(skipna=skipna)
    assert result is pd.NaT
    result = getattr(arr, name)(skipna=skipna)
    assert result is pd.NaT