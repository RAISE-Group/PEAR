@pytest.mark.parametrize('invalid_arr', ['[31337,]', '[,31337]', '[]]', '[,]'])
def test_decode_invalid_array(self, invalid_arr):
    with pytest.raises(ValueError):
        ujson.decode(invalid_arr)