@pytest.mark.parametrize('skipna', [True, False])
def test_min_max_with_nan(self, skipna):
    cat = Categorical([np.nan, 'b', 'c', np.nan], categories=['d', 'c', 'b', 'a'], ordered=True)
    _min = cat.min(skipna=skipna)
    _max = cat.max(skipna=skipna)
    if skipna is False:
        assert np.isnan(_min)
        assert np.isnan(_max)
    else:
        assert _min == 'c'
        assert _max == 'b'
    cat = Categorical([np.nan, 1, 2, np.nan], categories=[5, 4, 3, 2, 1], ordered=True)
    _min = cat.min(skipna=skipna)
    _max = cat.max(skipna=skipna)
    if skipna is False:
        assert np.isnan(_min)
        assert np.isnan(_max)
    else:
        assert _min == 2
        assert _max == 1