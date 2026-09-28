@pytest.mark.parametrize('invalid_dict', ['{{{{31337}}}}', '{{{{"key":}}}}', '{{{{"key"}}}}'])
def test_decode_invalid_dict(self, invalid_dict):
    with pytest.raises(ValueError):
        ujson.decode(invalid_dict)