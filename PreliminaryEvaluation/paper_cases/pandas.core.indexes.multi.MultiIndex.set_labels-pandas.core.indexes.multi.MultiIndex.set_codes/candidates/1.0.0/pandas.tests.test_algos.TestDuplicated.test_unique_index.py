def test_unique_index(self):
    cases = [Index([1, 2, 3]), pd.RangeIndex(0, 3)]
    for case in cases:
        assert case.is_unique is True
        tm.assert_numpy_array_equal(case.duplicated(), np.array([False, False, False]))