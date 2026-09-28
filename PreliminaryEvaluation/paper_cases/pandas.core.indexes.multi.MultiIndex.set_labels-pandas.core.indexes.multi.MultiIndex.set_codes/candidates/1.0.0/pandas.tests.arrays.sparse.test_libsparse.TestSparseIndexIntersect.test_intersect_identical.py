def test_intersect_identical(self):
    cases = [IntIndex(5, np.array([1, 2], dtype=np.int32)), IntIndex(5, np.array([0, 2, 4], dtype=np.int32)), IntIndex(0, np.array([], dtype=np.int32)), IntIndex(5, np.array([], dtype=np.int32))]
    for case in cases:
        assert case.intersect(case).equals(case)
        case = case.to_block_index()
        assert case.intersect(case).equals(case)