def test_get_unique_index(self, indices):
    if not len(indices) or isinstance(indices, MultiIndex):
        pytest.skip('Skip check for empty Index and MultiIndex')
    idx = indices[[0] * 5]
    idx_unique = indices[[0]]
    assert idx_unique.is_unique is True
    try:
        assert idx_unique.hasnans is False
    except NotImplementedError:
        pass
    for dropna in [False, True]:
        result = idx._get_unique_index(dropna=dropna)
        tm.assert_index_equal(result, idx_unique)
    if not indices._can_hold_na:
        pytest.skip('Skip na-check if index cannot hold na')
    if needs_i8_conversion(indices):
        vals = indices.asi8[[0] * 5]
        vals[0] = iNaT
    else:
        vals = indices.values[[0] * 5]
        vals[0] = np.nan
    vals_unique = vals[:2]
    idx_nan = indices._shallow_copy(vals)
    idx_unique_nan = indices._shallow_copy(vals_unique)
    assert idx_unique_nan.is_unique is True
    assert idx_nan.dtype == indices.dtype
    assert idx_unique_nan.dtype == indices.dtype
    for dropna, expected in zip([False, True], [idx_unique_nan, idx_unique]):
        for i in [idx_nan, idx_unique_nan]:
            result = i._get_unique_index(dropna=dropna)
            tm.assert_index_equal(result, expected)