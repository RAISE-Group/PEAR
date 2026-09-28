def test_series_default_orient(self):
    assert self.series.to_json() == self.series.to_json(orient='index')