@pytest.mark.parametrize('too_big_char', ['[', '{'])
def test_decode_depth_too_big(self, too_big_char):
    with pytest.raises(ValueError):
        ujson.decode(too_big_char * (1024 * 1024))