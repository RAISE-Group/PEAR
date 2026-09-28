@pytest.mark.parametrize('bool_input', [True, False])
def test_bool(self, bool_input):
    b = np.bool(bool_input)
    assert ujson.decode(ujson.encode(b)) == b