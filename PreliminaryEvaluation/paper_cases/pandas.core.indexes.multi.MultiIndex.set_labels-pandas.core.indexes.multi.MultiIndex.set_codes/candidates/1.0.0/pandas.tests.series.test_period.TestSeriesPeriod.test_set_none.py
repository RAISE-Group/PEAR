def test_set_none(self):
    self.series[3] = None
    assert self.series[3] is pd.NaT
    self.series[3:5] = None
    assert self.series[4] is pd.NaT