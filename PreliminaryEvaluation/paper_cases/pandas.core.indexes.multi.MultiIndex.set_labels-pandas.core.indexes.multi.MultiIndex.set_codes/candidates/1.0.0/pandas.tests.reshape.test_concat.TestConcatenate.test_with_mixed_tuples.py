def test_with_mixed_tuples(self, sort):
    df1 = DataFrame({'A': 'foo', ('B', 1): 'bar'}, index=range(2))
    df2 = DataFrame({'B': 'foo', ('B', 1): 'bar'}, index=range(2))
    concat([df1, df2], sort=sort)