@pytest.mark.parametrize('arr', [[], [31337]])
def test_decode_array(self, arr):
    assert arr == ujson.decode(str(arr))