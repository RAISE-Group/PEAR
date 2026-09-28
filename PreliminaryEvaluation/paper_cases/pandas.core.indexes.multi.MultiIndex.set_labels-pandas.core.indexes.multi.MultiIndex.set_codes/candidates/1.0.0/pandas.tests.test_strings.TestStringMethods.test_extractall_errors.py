def test_extractall_errors(self):
    s = Series(['a3', 'b3', 'd4c2'], name='series_name')
    with pytest.raises(ValueError, match='no capture groups'):
        s.str.extractall('[a-z]')