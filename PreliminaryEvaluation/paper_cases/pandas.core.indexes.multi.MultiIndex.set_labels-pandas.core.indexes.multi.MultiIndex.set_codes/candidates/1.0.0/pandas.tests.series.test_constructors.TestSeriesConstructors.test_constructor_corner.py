def test_constructor_corner(self):
    df = tm.makeTimeDataFrame()
    objs = [df, df]
    s = Series(objs, index=[0, 1])
    assert isinstance(s, Series)