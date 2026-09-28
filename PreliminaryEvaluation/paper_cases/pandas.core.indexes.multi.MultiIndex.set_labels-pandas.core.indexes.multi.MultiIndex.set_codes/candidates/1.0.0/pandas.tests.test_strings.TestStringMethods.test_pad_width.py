@pytest.mark.parametrize('f', ['center', 'ljust', 'rjust', 'zfill', 'pad'])
def test_pad_width(self, f):
    s = Series(['1', '22', 'a', 'bb'])
    msg = 'width must be of integer type, not*'
    with pytest.raises(TypeError, match=msg):
        getattr(s.str, f)('f')