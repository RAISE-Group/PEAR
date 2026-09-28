def test_tdarr_div_length_mismatch(self, box_with_array):
    rng = TimedeltaIndex(['1 days', pd.NaT, '2 days'])
    mismatched = [1, 2, 3, 4]
    rng = tm.box_expected(rng, box_with_array)
    for obj in [mismatched, mismatched[:2]]:
        for other in [obj, np.array(obj), pd.Index(obj)]:
            with pytest.raises(ValueError):
                rng / other
            with pytest.raises(ValueError):
                other / rng