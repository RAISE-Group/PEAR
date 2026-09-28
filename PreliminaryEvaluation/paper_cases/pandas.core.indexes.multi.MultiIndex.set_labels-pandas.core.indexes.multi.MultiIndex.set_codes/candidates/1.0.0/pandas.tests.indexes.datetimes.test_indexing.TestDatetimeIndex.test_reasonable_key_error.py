def test_reasonable_key_error(self):
    index = DatetimeIndex(['1/3/2000'])
    with pytest.raises(KeyError, match='2000'):
        index.get_loc('1/1/2000')