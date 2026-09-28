def test_iloc_exceeds_bounds(self):
    df = DataFrame(np.random.random_sample((20, 5)), columns=list('ABCDE'))
    msg = 'positional indexers are out-of-bounds'
    with pytest.raises(IndexError, match=msg):
        df.iloc[:, [0, 1, 2, 3, 4, 5]]
    with pytest.raises(IndexError, match=msg):
        df.iloc[[1, 30]]
    with pytest.raises(IndexError, match=msg):
        df.iloc[[1, -30]]
    with pytest.raises(IndexError, match=msg):
        df.iloc[[100]]
    s = df['A']
    with pytest.raises(IndexError, match=msg):
        s.iloc[[100]]
    with pytest.raises(IndexError, match=msg):
        s.iloc[[-100]]
    msg = 'single positional indexer is out-of-bounds'
    with pytest.raises(IndexError, match=msg):
        df.iloc[30]
    with pytest.raises(IndexError, match=msg):
        df.iloc[-30]
    with pytest.raises(IndexError, match=msg):
        s.iloc[30]
    with pytest.raises(IndexError, match=msg):
        s.iloc[-30]
    result = df.iloc[:, 4:10]
    expected = df.iloc[:, 4:]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[:, -4:-10]
    expected = df.iloc[:, :0]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[:, 10:4:-1]
    expected = df.iloc[:, :4:-1]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[:, 4:-10:-1]
    expected = df.iloc[:, 4::-1]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[:, -10:4]
    expected = df.iloc[:, :4]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[:, 10:4]
    expected = df.iloc[:, :0]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[:, -10:-11:-1]
    expected = df.iloc[:, :0]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[:, 10:11]
    expected = df.iloc[:, :0]
    tm.assert_frame_equal(result, expected)
    result = s.iloc[18:30]
    expected = s.iloc[18:]
    tm.assert_series_equal(result, expected)
    result = s.iloc[30:]
    expected = s.iloc[:0]
    tm.assert_series_equal(result, expected)
    result = s.iloc[30::-1]
    expected = s.iloc[::-1]
    tm.assert_series_equal(result, expected)

    def check(result, expected):
        str(result)
        result.dtypes
        tm.assert_frame_equal(result, expected)
    dfl = DataFrame(np.random.randn(5, 2), columns=list('AB'))
    check(dfl.iloc[:, 2:3], DataFrame(index=dfl.index))
    check(dfl.iloc[:, 1:3], dfl.iloc[:, [1]])
    check(dfl.iloc[4:6], dfl.iloc[[4]])
    msg = 'positional indexers are out-of-bounds'
    with pytest.raises(IndexError, match=msg):
        dfl.iloc[[4, 5, 6]]
    msg = 'single positional indexer is out-of-bounds'
    with pytest.raises(IndexError, match=msg):
        dfl.iloc[:, 4]