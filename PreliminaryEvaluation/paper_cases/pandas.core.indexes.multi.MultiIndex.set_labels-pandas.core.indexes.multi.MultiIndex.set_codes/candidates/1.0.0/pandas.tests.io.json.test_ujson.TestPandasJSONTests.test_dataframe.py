def test_dataframe(self, orient, numpy):
    if orient == 'records' and numpy:
        pytest.skip('Not idiomatic pandas')
    df = DataFrame([[1, 2, 3], [4, 5, 6]], index=['a', 'b'], columns=['x', 'y', 'z'])
    encode_kwargs = {} if orient is None else dict(orient=orient)
    decode_kwargs = {} if numpy is None else dict(numpy=numpy)
    output = ujson.decode(ujson.encode(df, **encode_kwargs), **decode_kwargs)
    if orient == 'split':
        dec = _clean_dict(output)
        output = DataFrame(**dec)
    else:
        output = DataFrame(output)
    if orient == 'values':
        df.columns = [0, 1, 2]
        df.index = [0, 1]
    elif orient == 'records':
        df.index = [0, 1]
    elif orient == 'index':
        df = df.transpose()
    tm.assert_frame_equal(output, df, check_dtype=False)