def setup_method(self, method):
    self.df = DataFrame({'A': np.arange(6, dtype='int64'), 'B': Series(list('aabbca')).astype(CDT(list('cab')))}).set_index('B')
    self.df2 = DataFrame({'A': np.arange(6, dtype='int64'), 'B': Series(list('aabbca')).astype(CDT(list('cabe')))}).set_index('B')
    self.df3 = DataFrame({'A': np.arange(6, dtype='int64'), 'B': Series([1, 1, 2, 1, 3, 2]).astype(CDT([3, 2, 1], ordered=True))}).set_index('B')
    self.df4 = DataFrame({'A': np.arange(6, dtype='int64'), 'B': Series([1, 1, 2, 1, 3, 2]).astype(CDT([3, 2, 1], ordered=False))}).set_index('B')