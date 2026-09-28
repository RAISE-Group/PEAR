def test_axis_dates(self):
    json = self.tsframe.to_json()
    result = read_json(json)
    tm.assert_frame_equal(result, self.tsframe)
    json = self.ts.to_json()
    result = read_json(json, typ='series')
    tm.assert_series_equal(result, self.ts, check_names=False)
    assert result.name is None