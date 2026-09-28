@pytest.mark.parametrize('subtype', ['int64', 'uint64'])
def test_subtype_integer(self, index, subtype):
    dtype = IntervalDtype(subtype)
    result = index.astype(dtype)
    expected = IntervalIndex.from_arrays(index.left.astype(subtype), index.right.astype(subtype), closed=index.closed)
    tm.assert_index_equal(result, expected)