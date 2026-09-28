@pytest.fixture(scope='function', autouse=True)
def setup(self, datapath):
    self.dirpath = datapath('io', 'json', 'data')
    self.ts = tm.makeTimeSeries()
    self.ts.name = 'ts'
    self.series = tm.makeStringSeries()
    self.series.name = 'series'
    self.objSeries = tm.makeObjectSeries()
    self.objSeries.name = 'objects'
    self.empty_series = Series([], index=[], dtype=np.float64)
    self.empty_frame = DataFrame()
    self.frame = _frame.copy()
    self.frame2 = _frame2.copy()
    self.intframe = _intframe.copy()
    self.tsframe = _tsframe.copy()
    self.mixed_frame = _mixed_frame.copy()
    self.categorical = _cat_frame.copy()
    yield
    del self.dirpath
    del self.ts
    del self.series
    del self.objSeries
    del self.empty_series
    del self.empty_frame
    del self.frame
    del self.frame2
    del self.intframe
    del self.tsframe
    del self.mixed_frame