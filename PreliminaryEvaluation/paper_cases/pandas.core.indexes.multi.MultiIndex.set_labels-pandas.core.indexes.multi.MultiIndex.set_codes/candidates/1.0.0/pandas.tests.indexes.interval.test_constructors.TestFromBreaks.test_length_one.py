def test_length_one(self):
    """breaks of length one produce an empty IntervalIndex"""
    breaks = [0]
    result = IntervalIndex.from_breaks(breaks)
    expected = IntervalIndex.from_breaks([])
    tm.assert_index_equal(result, expected)