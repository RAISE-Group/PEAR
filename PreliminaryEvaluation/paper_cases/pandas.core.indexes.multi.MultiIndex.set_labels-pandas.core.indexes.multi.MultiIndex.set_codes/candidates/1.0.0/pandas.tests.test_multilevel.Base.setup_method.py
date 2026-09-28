def setup_method(self, method):
    index = MultiIndex(levels=[['foo', 'bar', 'baz', 'qux'], ['one', 'two', 'three']], codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]], names=['first', 'second'])
    self.frame = DataFrame(np.random.randn(10, 3), index=index, columns=Index(['A', 'B', 'C'], name='exp'))
    self.single_level = MultiIndex(levels=[['foo', 'bar', 'baz', 'qux']], codes=[[0, 1, 2, 3]], names=['first'])
    arrays = [['bar', 'bar', 'baz', 'baz', 'qux', 'qux', 'foo', 'foo'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
    tuples = zip(*arrays)
    index = MultiIndex.from_tuples(tuples)
    s = Series(randn(8), index=index)
    s[3] = np.NaN
    self.series = s
    self.tdf = tm.makeTimeDataFrame(100)
    self.ymd = self.tdf.groupby([lambda x: x.year, lambda x: x.month, lambda x: x.day]).sum()
    self.ymd.index.set_levels([lev.astype('i8') for lev in self.ymd.index.levels], inplace=True)
    self.ymd.index.set_names(['year', 'month', 'day'], inplace=True)