def test_reset_index_with_drop(self):
    deleveled = self.ymd.reset_index(drop=True)
    assert len(deleveled.columns) == len(self.ymd.columns)
    assert deleveled.index.name == self.ymd.index.name
    deleveled = self.series.reset_index()
    assert isinstance(deleveled, DataFrame)
    assert len(deleveled.columns) == len(self.series.index.levels) + 1
    assert deleveled.index.name == self.series.index.name
    deleveled = self.series.reset_index(drop=True)
    assert isinstance(deleveled, Series)
    assert deleveled.index.name == self.series.index.name