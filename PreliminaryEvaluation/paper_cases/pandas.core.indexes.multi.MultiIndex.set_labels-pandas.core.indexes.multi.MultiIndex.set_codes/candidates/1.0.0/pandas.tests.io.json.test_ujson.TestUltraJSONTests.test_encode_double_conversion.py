@pytest.mark.parametrize('double_input', [math.pi, -math.pi])
def test_encode_double_conversion(self, double_input):
    output = ujson.encode(double_input)
    assert round(double_input, 5) == round(json.loads(output), 5)
    assert round(double_input, 5) == round(ujson.decode(output), 5)