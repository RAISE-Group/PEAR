def test_datetime_units(self):
    val = datetime.datetime(2013, 8, 17, 21, 17, 12, 215504)
    stamp = Timestamp(val)
    roundtrip = ujson.decode(ujson.encode(val, date_unit='s'))
    assert roundtrip == stamp.value // 10 ** 9
    roundtrip = ujson.decode(ujson.encode(val, date_unit='ms'))
    assert roundtrip == stamp.value // 10 ** 6
    roundtrip = ujson.decode(ujson.encode(val, date_unit='us'))
    assert roundtrip == stamp.value // 10 ** 3
    roundtrip = ujson.decode(ujson.encode(val, date_unit='ns'))
    assert roundtrip == stamp.value
    msg = "Invalid value 'foo' for option 'date_unit'"
    with pytest.raises(ValueError, match=msg):
        ujson.encode(val, date_unit='foo')