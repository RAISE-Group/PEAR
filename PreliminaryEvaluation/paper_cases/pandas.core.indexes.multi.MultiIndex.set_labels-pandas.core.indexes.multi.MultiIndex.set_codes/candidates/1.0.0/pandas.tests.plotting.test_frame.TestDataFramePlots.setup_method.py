def setup_method(self, method):
    TestPlotBase.setup_method(self, method)
    import matplotlib as mpl
    mpl.rcdefaults()
    self.tdf = tm.makeTimeDataFrame()
    self.hexbin_df = DataFrame({'A': np.random.uniform(size=20), 'B': np.random.uniform(size=20), 'C': np.arange(20) + np.random.uniform(size=20)})