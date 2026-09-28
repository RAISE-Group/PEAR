@pytest.mark.parametrize('broken_json', ['[', '{', ']', '}'])
def test_decode_broken_json(self, broken_json):
    with pytest.raises(ValueError):
        ujson.decode(broken_json)