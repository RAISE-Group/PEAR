def setup_method(self, method):
    self.df = DataFrame({'key1': get_test_data(), 'key2': get_test_data(), 'data1': np.random.randn(N), 'data2': np.random.randn(N)})
    self.df = self.df[self.df['key2'] > 1]
    self.df2 = DataFrame({'key1': get_test_data(n=N // 5), 'key2': get_test_data(ngroups=NGROUPS // 2, n=N // 5), 'value': np.random.randn(N // 5)})
    self.left = DataFrame({'key': ['a', 'b', 'c', 'd', 'e', 'e', 'a'], 'v1': np.random.randn(7)})
    self.right = DataFrame({'v2': np.random.randn(4)}, index=['d', 'b', 'c', 'a'])