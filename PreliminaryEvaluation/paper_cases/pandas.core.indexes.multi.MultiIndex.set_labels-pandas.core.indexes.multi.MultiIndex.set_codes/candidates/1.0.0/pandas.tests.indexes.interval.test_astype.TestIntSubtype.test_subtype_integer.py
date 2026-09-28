@pytest.mark.parametrize('subtype_start, subtype_end', [('int64', 'uint64'), ('uint64', 'int64')])
def test_subtype_integer(self, subtype_start, subtype_end):
    index = IntervalIndex.from_breaks(np.arange(100, dtype=subtype_start))
    dtype = IntervalDtype(subtype_end)
    result = index.astype(dtype)
    expected = IntervalIndex.from_arrays(index.left.astype(subtype_end), index.right.astype(subtype_end), closed=index.closed)
    tm.assert_index_equal(result, expected)