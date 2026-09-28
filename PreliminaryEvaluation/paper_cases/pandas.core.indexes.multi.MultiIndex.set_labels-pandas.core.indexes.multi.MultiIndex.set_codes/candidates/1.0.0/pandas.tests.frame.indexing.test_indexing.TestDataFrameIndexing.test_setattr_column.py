def test_setattr_column(self):
    df = DataFrame({'foobar': 1}, index=range(10))
    df.foobar = 5
    assert (df.foobar == 5).all()