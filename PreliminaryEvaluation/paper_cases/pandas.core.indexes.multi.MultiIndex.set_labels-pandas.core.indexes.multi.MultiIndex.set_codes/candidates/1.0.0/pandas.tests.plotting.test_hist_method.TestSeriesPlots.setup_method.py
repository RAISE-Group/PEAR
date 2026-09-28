def setup_method(self, method):
    TestPlotBase.setup_method(self, method)
    import matplotlib as mpl
    mpl.rcdefaults()
    self.ts = tm.makeTimeSeries()
    self.ts.name = 'ts'