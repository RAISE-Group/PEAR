@pytest.mark.parametrize('left_subtype, right_subtype', [(np.int64, np.float64), (np.float64, np.int64)])
def test_mixed_float_int(self, left_subtype, right_subtype):
    """mixed int/float left/right results in float for both sides"""
    left = np.arange(9, dtype=left_subtype)
    right = np.arange(1, 10, dtype=right_subtype)
    result = IntervalIndex.from_arrays(left, right)
    expected_left = Float64Index(left)
    expected_right = Float64Index(right)
    expected_subtype = np.float64
    tm.assert_index_equal(result.left, expected_left)
    tm.assert_index_equal(result.right, expected_right)
    assert result.dtype.subtype == expected_subtype