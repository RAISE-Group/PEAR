def test_no_new_globals(self, engine, parser):
    x = 1
    gbls = globals().copy()
    pd.eval('x + 1', engine=engine, parser=parser)
    gbls2 = globals().copy()
    assert gbls == gbls2