def test_get_loc_raises_missized_tolerance(self):
    index = pd.Index([0, 1, 2])
    with pytest.raises(ValueError, match='tolerance size must match'):
        index.get_loc(1.1, 'nearest', tolerance=[1, 1])