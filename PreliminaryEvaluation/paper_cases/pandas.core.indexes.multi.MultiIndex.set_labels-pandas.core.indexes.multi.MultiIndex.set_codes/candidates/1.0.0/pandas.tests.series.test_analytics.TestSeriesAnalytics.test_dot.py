def test_dot(self):
    a = Series(np.random.randn(4), index=['p', 'q', 'r', 's'])
    b = DataFrame(np.random.randn(3, 4), index=['1', '2', '3'], columns=['p', 'q', 'r', 's']).T
    result = a.dot(b)
    expected = Series(np.dot(a.values, b.values), index=['1', '2', '3'])
    tm.assert_series_equal(result, expected)
    b2 = b.reindex(index=reversed(b.index))
    result = a.dot(b)
    tm.assert_series_equal(result, expected)
    result = a.dot(b.values)
    assert np.all(result == expected.values)
    tm.assert_almost_equal(a.dot(b['2'].values), expected['2'])
    tm.assert_almost_equal(a.dot(b['1']), expected['1'])
    tm.assert_almost_equal(a.dot(b2['1']), expected['1'])
    msg = 'Dot product shape mismatch, \\(4,\\) vs \\(3,\\)'
    with pytest.raises(Exception, match=msg):
        a.dot(a.values[:3])
    msg = 'matrices are not aligned'
    with pytest.raises(ValueError, match=msg):
        a.dot(b.T)