def test_map(self):
    index = PeriodIndex([2005, 2007, 2009], freq='A')
    result = index.map(lambda x: x.ordinal)
    exp = Index([x.ordinal for x in index])
    tm.assert_index_equal(result, exp)