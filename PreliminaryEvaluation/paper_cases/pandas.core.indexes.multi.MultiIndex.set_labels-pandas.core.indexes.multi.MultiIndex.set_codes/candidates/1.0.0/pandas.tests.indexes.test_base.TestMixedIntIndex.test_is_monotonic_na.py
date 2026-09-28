@pytest.mark.parametrize('index', [pd.Index([np.nan]), pd.Index([np.nan, 1]), pd.Index([1, 2, np.nan]), pd.Index(['a', 'b', np.nan]), pd.to_datetime(['NaT']), pd.to_datetime(['NaT', '2000-01-01']), pd.to_datetime(['2000-01-01', 'NaT', '2000-01-02']), pd.to_timedelta(['1 day', 'NaT'])])
def test_is_monotonic_na(self, index):
    assert index.is_monotonic_increasing is False
    assert index.is_monotonic_decreasing is False
    assert index._is_strictly_monotonic_increasing is False
    assert index._is_strictly_monotonic_decreasing is False