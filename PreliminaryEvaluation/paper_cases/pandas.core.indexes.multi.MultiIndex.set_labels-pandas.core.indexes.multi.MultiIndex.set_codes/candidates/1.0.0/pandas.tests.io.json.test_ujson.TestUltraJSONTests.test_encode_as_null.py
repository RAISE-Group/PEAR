@pytest.mark.parametrize('decoded_input', [NaT, np.datetime64('NaT'), np.nan, np.inf, -np.inf])
def test_encode_as_null(self, decoded_input):
    assert ujson.encode(decoded_input) == 'null', 'Expected null'