def test_apply_args(self):
    s = Series(['foo,bar'])
    result = s.apply(str.split, args=(',',))
    assert result[0] == ['foo', 'bar']
    assert isinstance(result[0], list)