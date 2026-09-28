@pytest.mark.parametrize('subtype', ['int64', 'uint64'])
def test_subtype_integer(self, subtype):
    index = interval_range(0.0, 10.0)
    dtype = IntervalDtype(subtype)
    result = index.astype(dtype)
    expected = IntervalIndex.from_arrays(index.left.astype(subtype), index.right.astype(subtype), closed=index.closed)
    tm.assert_index_equal(result, expected)
    msg = 'Cannot convert non-finite values \\(NA or inf\\) to integer'
    with pytest.raises(ValueError, match=msg):
        index.insert(0, np.nan).astype(dtype)