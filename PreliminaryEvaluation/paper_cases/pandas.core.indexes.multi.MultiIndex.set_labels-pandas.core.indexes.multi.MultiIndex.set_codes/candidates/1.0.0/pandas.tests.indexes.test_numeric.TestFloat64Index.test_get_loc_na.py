def test_get_loc_na(self):
    idx = Float64Index([np.nan, 1, 2])
    assert idx.get_loc(1) == 1
    assert idx.get_loc(np.nan) == 0
    idx = Float64Index([np.nan, 1, np.nan])
    assert idx.get_loc(1) == 1
    sliced = idx.slice_locs(np.nan)
    assert isinstance(sliced, tuple)
    assert sliced == (0, 3)
    idx = Float64Index([np.nan, 1, np.nan, np.nan])
    assert idx.get_loc(1) == 1
    msg = "'Cannot get left slice bound for non-unique label: nan"
    with pytest.raises(KeyError, match=msg):
        idx.slice_locs(np.nan)