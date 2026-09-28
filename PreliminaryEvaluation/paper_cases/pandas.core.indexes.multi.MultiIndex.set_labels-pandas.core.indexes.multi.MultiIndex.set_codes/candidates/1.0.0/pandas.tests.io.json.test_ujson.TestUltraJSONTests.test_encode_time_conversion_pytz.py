def test_encode_time_conversion_pytz(self):
    test = datetime.time(10, 12, 15, 343243, pytz.utc)
    output = ujson.encode(test)
    expected = f'"{test.isoformat()}"'
    assert expected == output