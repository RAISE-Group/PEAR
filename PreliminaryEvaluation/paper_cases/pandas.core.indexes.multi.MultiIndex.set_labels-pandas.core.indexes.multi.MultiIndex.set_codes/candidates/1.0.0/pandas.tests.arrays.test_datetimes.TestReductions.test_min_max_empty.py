@pytest.mark.parametrize('tz', [None, 'US/Central'])
@pytest.mark.parametrize('skipna', [True, False])
def test_min_max_empty(self, skipna, tz):
    arr = DatetimeArray._from_sequence([], tz=tz)
    result = arr.min(skipna=skipna)
    assert result is pd.NaT
    result = arr.max(skipna=skipna)
    assert result is pd.NaT