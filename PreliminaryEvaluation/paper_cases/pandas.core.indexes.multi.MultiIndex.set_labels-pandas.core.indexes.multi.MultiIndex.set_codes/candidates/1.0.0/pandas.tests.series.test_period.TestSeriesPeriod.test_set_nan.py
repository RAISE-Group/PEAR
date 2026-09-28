def test_set_nan(self):
    self.series[5] = np.nan
    assert self.series[5] is pd.NaT
    self.series[5:7] = np.nan
    assert self.series[6] is pd.NaT