def test_groupby_corner(self):
    midx = MultiIndex(levels=[['foo'], ['bar'], ['baz']], codes=[[0], [0], [0]], names=['one', 'two', 'three'])
    df = DataFrame([np.random.rand(4)], columns=['a', 'b', 'c', 'd'], index=midx)
    df.groupby(level='three')