def setup_method(self, method):
    TestPlotBase.setup_method(self, method)
    import matplotlib as mpl
    mpl.rcdefaults()
    self.ts = tm.makeTimeSeries()
    self.ts.name = 'ts'
    self.series = tm.makeStringSeries()
    self.series.name = 'series'
    self.iseries = tm.makePeriodSeries()
    self.iseries.name = 'iseries'