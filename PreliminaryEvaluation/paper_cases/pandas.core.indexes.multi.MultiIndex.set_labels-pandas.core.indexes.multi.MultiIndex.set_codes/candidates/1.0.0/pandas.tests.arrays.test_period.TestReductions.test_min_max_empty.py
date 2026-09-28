@pytest.mark.parametrize('skipna', [True, False])
def test_min_max_empty(self, skipna):
    arr = period_array([], freq='D')
    result = arr.min(skipna=skipna)
    assert result is pd.NaT
    result = arr.max(skipna=skipna)
    assert result is pd.NaT