def test_repr_unicode(self):
    s = Series(['σ'] * 10)
    repr(s)
    a = Series(['א'] * 1000)
    a.name = 'title1'
    repr(a)