def test_decode_jibberish(self):
    jibberish = 'fdsa sda v9sa fdsa'
    with pytest.raises(ValueError):
        ujson.decode(jibberish)