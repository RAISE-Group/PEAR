def test_append(self, appends):
    indices, expected = appends
    result = indices[0].append(indices[1:])
    tm.assert_index_equal(result, expected, exact=True)
    if len(indices) == 2:
        result2 = indices[0].append(indices[1])
        tm.assert_index_equal(result2, expected, exact=True)