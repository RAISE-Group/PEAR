def test_get_loc_tolerance_no_method_raises(self):
    index = pd.Index([0, 1, 2])
    with pytest.raises(ValueError, match='tolerance .* valid if'):
        index.get_loc(1.1, tolerance=1)