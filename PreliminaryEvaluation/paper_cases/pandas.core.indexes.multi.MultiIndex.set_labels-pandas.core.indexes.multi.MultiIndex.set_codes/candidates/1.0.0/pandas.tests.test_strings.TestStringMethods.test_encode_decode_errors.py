def test_encode_decode_errors(self):
    encodeBase = Series(['a', 'b', 'a\x9d'])
    msg = "'charmap' codec can't encode character '\\\\x9d' in position 1: character maps to <undefined>"
    with pytest.raises(UnicodeEncodeError, match=msg):
        encodeBase.str.encode('cp1252')
    f = lambda x: x.encode('cp1252', 'ignore')
    result = encodeBase.str.encode('cp1252', 'ignore')
    exp = encodeBase.map(f)
    tm.assert_series_equal(result, exp)
    decodeBase = Series([b'a', b'b', b'a\x9d'])
    msg = "'charmap' codec can't decode byte 0x9d in position 1: character maps to <undefined>"
    with pytest.raises(UnicodeDecodeError, match=msg):
        decodeBase.str.decode('cp1252')
    f = lambda x: x.decode('cp1252', 'ignore')
    result = decodeBase.str.decode('cp1252', 'ignore')
    exp = decodeBase.map(f)
    tm.assert_series_equal(result, exp)