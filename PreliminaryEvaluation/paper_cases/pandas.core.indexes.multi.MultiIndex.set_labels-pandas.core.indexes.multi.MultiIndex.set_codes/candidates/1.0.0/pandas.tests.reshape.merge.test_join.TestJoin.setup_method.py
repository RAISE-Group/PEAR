def setup_method(self, method):
    self.df = DataFrame({'key1': get_test_data(), 'key2': get_test_data(), 'data1': np.random.randn(N), 'data2': np.random.randn(N)})
    self.df = self.df[self.df['key2'] > 1]
    self.df2 = DataFrame({'key1': get_test_data(n=N // 5), 'key2': get_test_data(ngroups=NGROUPS // 2, n=N // 5), 'value': np.random.randn(N // 5)})
    index, data = tm.getMixedTypeDict()
    self.target = DataFrame(data, index=index)
    self.source = DataFrame({'MergedA': data['A'], 'MergedD': data['D']}, index=data['C'])