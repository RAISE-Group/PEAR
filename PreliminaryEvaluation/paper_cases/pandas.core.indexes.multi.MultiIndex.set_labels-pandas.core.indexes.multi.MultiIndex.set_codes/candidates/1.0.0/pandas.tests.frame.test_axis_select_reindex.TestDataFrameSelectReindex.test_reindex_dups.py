def test_reindex_dups(self):
    arr = np.random.randn(10)
    df = DataFrame(arr, index=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    result = df.copy()
    result.index = list(range(len(df)))
    expected = DataFrame(arr, index=list(range(len(df))))
    tm.assert_frame_equal(result, expected)
    msg = 'cannot reindex from a duplicate axis'
    with pytest.raises(ValueError, match=msg):
        df.reindex(index=list(range(len(df))))