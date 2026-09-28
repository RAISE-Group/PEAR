@pytest.mark.parametrize('extreme_num', [9223372036854775807, -9223372036854775808])
def test_decode_extreme_numbers(self, extreme_num):
    assert extreme_num == ujson.decode(str(extreme_num))