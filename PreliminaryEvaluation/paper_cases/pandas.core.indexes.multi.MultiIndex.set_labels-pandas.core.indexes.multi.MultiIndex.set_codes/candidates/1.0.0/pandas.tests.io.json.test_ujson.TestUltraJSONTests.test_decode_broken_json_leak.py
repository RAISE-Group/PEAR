@pytest.mark.parametrize('broken_json', ['{{1337:""}}', '{{"key":"}', '[[[true'])
def test_decode_broken_json_leak(self, broken_json):
    for _ in range(1000):
        with pytest.raises(ValueError):
            ujson.decode(broken_json)