@pytest.mark.parametrize('long_number', [-4342969734183514, -12345678901234.568, -528656961.4399388])
def test_double_long_numbers(self, long_number):
    sut = {'a': long_number}
    encoded = ujson.encode(sut, double_precision=15)
    decoded = ujson.decode(encoded)
    assert sut == decoded