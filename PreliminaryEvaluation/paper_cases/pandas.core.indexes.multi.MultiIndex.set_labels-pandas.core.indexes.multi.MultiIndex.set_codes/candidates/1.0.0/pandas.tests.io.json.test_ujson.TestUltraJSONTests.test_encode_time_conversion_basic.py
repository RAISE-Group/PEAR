@pytest.mark.parametrize('test', [datetime.time(), datetime.time(1, 2, 3), datetime.time(10, 12, 15, 343243)])
def test_encode_time_conversion_basic(self, test):
    output = ujson.encode(test)
    expected = f'"{test.isoformat()}"'
    assert expected == output