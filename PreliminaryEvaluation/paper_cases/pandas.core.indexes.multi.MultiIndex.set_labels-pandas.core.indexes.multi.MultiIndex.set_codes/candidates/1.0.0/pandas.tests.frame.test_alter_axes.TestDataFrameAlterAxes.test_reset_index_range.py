def test_reset_index_range(self):
    df = DataFrame([[0, 0], [1, 1]], columns=['A', 'B'], index=RangeIndex(stop=2))
    result = df.reset_index()
    assert isinstance(result.index, RangeIndex)
    expected = DataFrame([[0, 0, 0], [1, 1, 1]], columns=['index', 'A', 'B'], index=RangeIndex(stop=2))
    tm.assert_frame_equal(result, expected)