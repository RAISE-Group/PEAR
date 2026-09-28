def test_get_loc_bad_tolerance_raises(self):
    index = pd.Index([0, 1, 2])
    with pytest.raises(ValueError, match='must be numeric'):
        index.get_loc(1.1, 'nearest', tolerance='invalid')