def test_encode_time_conversion_dateutil(self):
    test = datetime.time(10, 12, 15, 343243, dateutil.tz.tzutc())
    output = ujson.encode(test)
    expected = f'"{test.isoformat()}"'
    assert expected == output