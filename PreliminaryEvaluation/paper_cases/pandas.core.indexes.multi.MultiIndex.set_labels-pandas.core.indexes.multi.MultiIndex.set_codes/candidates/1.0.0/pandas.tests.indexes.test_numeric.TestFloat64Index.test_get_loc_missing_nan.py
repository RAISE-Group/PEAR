def test_get_loc_missing_nan(self):
    idx = Float64Index([1, 2])
    assert idx.get_loc(1) == 0
    with pytest.raises(KeyError, match='^3\\.0$'):
        idx.get_loc(3)
    with pytest.raises(KeyError, match='^nan$'):
        idx.get_loc(np.nan)
    with pytest.raises(KeyError, match='^\\[nan\\]$'):
        idx.get_loc([np.nan])