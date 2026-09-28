def test_searchsorted_monotonic(self, indices):
    if isinstance(indices, (MultiIndex, pd.IntervalIndex)):
        pytest.skip('Skip check for MultiIndex/IntervalIndex')
    if indices.empty:
        pytest.skip('Skip check for empty Index')
    value = indices[0]
    expected_left, expected_right = (0, (indices == value).argmin())
    if expected_right == 0:
        expected_right = len(indices)
    if indices.is_monotonic_increasing:
        ssm_left = indices._searchsorted_monotonic(value, side='left')
        assert expected_left == ssm_left
        ssm_right = indices._searchsorted_monotonic(value, side='right')
        assert expected_right == ssm_right
        ss_left = indices.searchsorted(value, side='left')
        assert expected_left == ss_left
        ss_right = indices.searchsorted(value, side='right')
        assert expected_right == ss_right
    elif indices.is_monotonic_decreasing:
        ssm_left = indices._searchsorted_monotonic(value, side='left')
        assert expected_left == ssm_left
        ssm_right = indices._searchsorted_monotonic(value, side='right')
        assert expected_right == ssm_right
    else:
        with pytest.raises(ValueError):
            indices._searchsorted_monotonic(value, side='left')