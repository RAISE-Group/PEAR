def setup_method(self):
    self.ts = tm.makeTimeSeries()
    self.ts.name = 'ts'
    self.series = tm.makeStringSeries()
    self.series.name = 'series'