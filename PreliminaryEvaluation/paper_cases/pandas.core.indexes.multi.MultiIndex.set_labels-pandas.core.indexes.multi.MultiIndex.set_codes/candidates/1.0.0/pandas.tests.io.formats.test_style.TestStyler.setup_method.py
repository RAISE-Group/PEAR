def setup_method(self, method):
    np.random.seed(24)
    self.s = DataFrame({'A': np.random.permutation(range(6))})
    self.df = DataFrame({'A': [0, 1], 'B': np.random.randn(2)})
    self.f = lambda x: x
    self.g = lambda x: x

    def h(x, foo='bar'):
        return pd.Series(f'color: {foo}', index=x.index, name=x.name)
    self.h = h
    self.styler = Styler(self.df)
    self.attrs = pd.DataFrame({'A': ['color: red', 'color: blue']})
    self.dataframes = [self.df, pd.DataFrame({'f': [1.0, 2.0], 'o': ['a', 'b'], 'c': pd.Categorical(['a', 'b'])})]