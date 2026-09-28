def test_cant_or_shouldnt_cast(self):
    with pytest.raises(TypeError):
        RangeIndex('foo', 'bar', 'baz')
    with pytest.raises(TypeError):
        RangeIndex('0', '1', '2')