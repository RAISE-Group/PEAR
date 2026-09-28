def test_decode_with_trailing_non_whitespaces(self):
    with pytest.raises(ValueError):
        ujson.decode('{}\n\t a')