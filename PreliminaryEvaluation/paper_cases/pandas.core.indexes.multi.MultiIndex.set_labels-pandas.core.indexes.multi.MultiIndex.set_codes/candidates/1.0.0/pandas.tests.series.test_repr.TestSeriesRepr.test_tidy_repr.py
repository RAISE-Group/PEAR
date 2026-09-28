def test_tidy_repr(self):
    a = Series(['א'] * 1000)
    a.name = 'title1'
    repr(a)