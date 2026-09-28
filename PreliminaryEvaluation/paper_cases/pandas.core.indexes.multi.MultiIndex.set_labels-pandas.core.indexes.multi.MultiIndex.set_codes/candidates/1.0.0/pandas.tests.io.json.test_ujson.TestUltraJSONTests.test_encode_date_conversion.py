def test_encode_date_conversion(self):
    date_input = datetime.date.fromtimestamp(time.time())
    output = ujson.encode(date_input, date_unit='s')
    tup = (date_input.year, date_input.month, date_input.day, 0, 0, 0)
    expected = calendar.timegm(tup)
    assert int(expected) == json.loads(output)
    assert int(expected) == ujson.decode(output)