@pytest.mark.parametrize('too_extreme_num', ['9223372036854775808', '-90223372036854775809'])
def test_decode_too_extreme_numbers(self, too_extreme_num):
    with pytest.raises(ValueError):
        ujson.decode(too_extreme_num)