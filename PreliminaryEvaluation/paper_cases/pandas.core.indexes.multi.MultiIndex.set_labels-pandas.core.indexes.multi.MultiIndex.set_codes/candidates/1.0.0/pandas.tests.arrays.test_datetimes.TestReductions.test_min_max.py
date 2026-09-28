@pytest.mark.parametrize('tz', [None, 'US/Central'])
def test_min_max(self, tz):
    arr = DatetimeArray._from_sequence(['2000-01-03', '2000-01-03', 'NaT', '2000-01-02', '2000-01-05', '2000-01-04'], tz=tz)
    result = arr.min()
    expected = pd.Timestamp('2000-01-02', tz=tz)
    assert result == expected
    result = arr.max()
    expected = pd.Timestamp('2000-01-05', tz=tz)
    assert result == expected
    result = arr.min(skipna=False)
    assert result is pd.NaT
    result = arr.max(skipna=False)
    assert result is pd.NaT