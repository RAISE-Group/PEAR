def test_cant_or_shouldnt_cast(self):
    msg = 'String dtype not supported, you may need to explicitly cast to a numeric type'
    data = ['foo', 'bar', 'baz']
    with pytest.raises(TypeError, match=msg):
        self._holder(data)
    data = ['0', '1', '2']
    with pytest.raises(TypeError, match=msg):
        self._holder(data)