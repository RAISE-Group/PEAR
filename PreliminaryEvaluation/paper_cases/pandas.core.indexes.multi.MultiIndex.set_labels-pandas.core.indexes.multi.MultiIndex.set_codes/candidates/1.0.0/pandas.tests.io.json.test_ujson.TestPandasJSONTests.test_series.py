def test_series(self, orient, numpy):
    s = Series([10, 20, 30, 40, 50, 60], name='series', index=[6, 7, 8, 9, 10, 15]).sort_values()
    encode_kwargs = {} if orient is None else dict(orient=orient)
    decode_kwargs = {} if numpy is None else dict(numpy=numpy)
    output = ujson.decode(ujson.encode(s, **encode_kwargs), **decode_kwargs)
    if orient == 'split':
        dec = _clean_dict(output)
        output = Series(**dec)
    else:
        output = Series(output)
    if orient in (None, 'index'):
        s.name = None
        output = output.sort_values()
        s.index = ['6', '7', '8', '9', '10', '15']
    elif orient in ('records', 'values'):
        s.name = None
        s.index = [0, 1, 2, 3, 4, 5]
    tm.assert_series_equal(output, s, check_dtype=False)