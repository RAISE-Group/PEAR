@pytest.mark.parametrize('dropna, expected', [(True, Series([], dtype=np.float64)), (False, Series([], dtype=np.float64))])
def test_mode_empty(self, dropna, expected):
    s = Series([], dtype=np.float64)
    result = s.mode(dropna)
    tm.assert_series_equal(result, expected)