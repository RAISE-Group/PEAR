@pytest.mark.parametrize('int_exp', ['1337E40', '1.337E40', '1337E+9', '1.337e+40', '1.337E-4'])
def test_decode_numeric_int_exp(self, int_exp):
    assert ujson.decode(int_exp) == json.loads(int_exp)