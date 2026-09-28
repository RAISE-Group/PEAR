def test_attrs(self):
    s = pd.Series([0, 1], name='abc')
    assert s.attrs == {}
    s.attrs['version'] = 1
    result = s + 1
    assert result.attrs == {'version': 1}