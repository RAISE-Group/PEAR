def setup_method(self, method):
    self.df = tm.makeTimeDataFrame()[:10]
    self.df['id1'] = (self.df['A'] > 0).astype(np.int64)
    self.df['id2'] = (self.df['B'] > 0).astype(np.int64)
    self.var_name = 'var'
    self.value_name = 'val'
    self.df1 = pd.DataFrame([[1.067683, -1.110463, 0.20867], [-1.321405, 0.368915, -1.055342], [-0.807333, 0.08298, -0.873361]])
    self.df1.columns = [list('ABC'), list('abc')]
    self.df1.columns.names = ['CAP', 'low']