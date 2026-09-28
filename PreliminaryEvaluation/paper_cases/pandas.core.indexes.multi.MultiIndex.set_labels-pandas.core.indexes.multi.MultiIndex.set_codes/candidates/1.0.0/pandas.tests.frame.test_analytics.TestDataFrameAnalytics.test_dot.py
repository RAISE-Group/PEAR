def test_dot(self):
    a = DataFrame(np.random.randn(3, 4), index=['a', 'b', 'c'], columns=['p', 'q', 'r', 's'])
    b = DataFrame(np.random.randn(4, 2), index=['p', 'q', 'r', 's'], columns=['one', 'two'])
    result = a.dot(b)
    expected = DataFrame(np.dot(a.values, b.values), index=['a', 'b', 'c'], columns=['one', 'two'])
    b1 = b.reindex(index=reversed(b.index))
    result = a.dot(b)
    tm.assert_frame_equal(result, expected)
    result = a.dot(b['one'])
    tm.assert_series_equal(result, expected['one'], check_names=False)
    assert result.name is None
    result = a.dot(b1['one'])
    tm.assert_series_equal(result, expected['one'], check_names=False)
    assert result.name is None
    row = a.iloc[0].values
    result = a.dot(row)
    expected = a.dot(a.iloc[0])
    tm.assert_series_equal(result, expected)
    with pytest.raises(ValueError, match='Dot product shape mismatch'):
        a.dot(row[:-1])
    a = np.random.rand(1, 5)
    b = np.random.rand(5, 1)
    A = DataFrame(a)
    B = DataFrame(b)
    result = A.dot(b)
    df = DataFrame(np.random.randn(3, 4), index=[1, 2, 3], columns=range(4))
    df2 = DataFrame(np.random.randn(5, 3), index=range(5), columns=[1, 2, 3])
    with pytest.raises(ValueError, match='aligned'):
        df.dot(df2)