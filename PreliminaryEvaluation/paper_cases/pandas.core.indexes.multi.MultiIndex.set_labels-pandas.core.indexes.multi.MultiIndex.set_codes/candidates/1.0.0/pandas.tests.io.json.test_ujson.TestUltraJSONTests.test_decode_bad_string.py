@pytest.mark.parametrize('bad_string', ['"TESTING', '"TESTING\\"', 'tru', 'fa', 'n'])
def test_decode_bad_string(self, bad_string):
    with pytest.raises(ValueError):
        ujson.decode(bad_string)