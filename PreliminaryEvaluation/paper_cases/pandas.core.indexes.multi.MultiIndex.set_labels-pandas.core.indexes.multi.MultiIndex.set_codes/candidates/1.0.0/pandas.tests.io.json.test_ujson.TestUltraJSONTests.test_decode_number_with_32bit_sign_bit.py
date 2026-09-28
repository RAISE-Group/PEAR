@pytest.mark.parametrize('val', [3590016419, 2 ** 31, 2 ** 32, 2 ** 32 - 1])
def test_decode_number_with_32bit_sign_bit(self, val):
    doc = f'{{"id": {val}}}'
    assert ujson.decode(doc)['id'] == val