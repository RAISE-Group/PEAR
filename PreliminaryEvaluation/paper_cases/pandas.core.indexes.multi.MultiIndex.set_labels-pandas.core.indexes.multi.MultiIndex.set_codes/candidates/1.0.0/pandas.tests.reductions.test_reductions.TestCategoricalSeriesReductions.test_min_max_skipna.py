@pytest.mark.parametrize('skipna', [True, False])
def test_min_max_skipna(self, skipna):
    cat = Series(Categorical(['a', 'b', np.nan, 'a'], categories=['b', 'a'], ordered=True))
    _min = cat.min(skipna=skipna)
    _max = cat.max(skipna=skipna)
    if skipna is True:
        assert _min == 'b'
        assert _max == 'a'
    else:
        assert np.isnan(_min)
        assert np.isnan(_max)