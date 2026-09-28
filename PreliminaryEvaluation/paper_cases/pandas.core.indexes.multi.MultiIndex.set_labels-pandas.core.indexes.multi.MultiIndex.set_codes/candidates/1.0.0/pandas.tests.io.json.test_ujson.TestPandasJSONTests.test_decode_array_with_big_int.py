def test_decode_array_with_big_int(self):
    with pytest.raises(ValueError):
        ujson.loads('[18446098363113800555]')