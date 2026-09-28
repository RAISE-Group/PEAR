@pytest.mark.parametrize('index', ['string', 'int', 'float'], indirect=True)
@pytest.mark.parametrize('keys', [['foo', 'bar'], ['1', 'bar']])
def test_drop_by_str_label_raises_missing_keys(self, index, keys):
    with pytest.raises(KeyError, match=''):
        index.drop(keys)