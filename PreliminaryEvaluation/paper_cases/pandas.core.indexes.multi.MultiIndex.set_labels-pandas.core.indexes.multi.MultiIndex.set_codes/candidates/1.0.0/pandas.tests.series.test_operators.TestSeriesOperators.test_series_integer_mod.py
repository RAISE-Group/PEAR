@pytest.mark.parametrize('index', [None, range(9)])
def test_series_integer_mod(self, index):
    s1 = Series(range(1, 10))
    s2 = Series('foo', index=index)
    msg = 'not all arguments converted during string formatting'
    with pytest.raises(TypeError, match=msg):
        s2 % s1