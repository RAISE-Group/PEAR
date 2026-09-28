@pytest.mark.parametrize('unicode_key', ['key1', 'بن'])
def test_encode_dict_with_unicode_keys(self, unicode_key):
    unicode_dict = {unicode_key: 'value1'}
    assert unicode_dict == ujson.decode(ujson.encode(unicode_dict))