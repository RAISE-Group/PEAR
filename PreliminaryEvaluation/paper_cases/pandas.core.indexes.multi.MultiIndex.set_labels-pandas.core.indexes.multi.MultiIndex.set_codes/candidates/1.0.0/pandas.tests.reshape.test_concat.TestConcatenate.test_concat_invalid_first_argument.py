def test_concat_invalid_first_argument(self):
    df1 = tm.makeCustomDataframe(10, 2)
    df2 = tm.makeCustomDataframe(10, 2)
    msg = 'first argument must be an iterable of pandas objects, you passed an object of type "DataFrame"'
    with pytest.raises(TypeError, match=msg):
        concat(df1, df2)
    concat((DataFrame(np.random.rand(5, 5)) for _ in range(3)))
    data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
    reader = read_csv(StringIO(data), chunksize=1)
    result = concat(reader, ignore_index=True)
    expected = read_csv(StringIO(data))
    tm.assert_frame_equal(result, expected)