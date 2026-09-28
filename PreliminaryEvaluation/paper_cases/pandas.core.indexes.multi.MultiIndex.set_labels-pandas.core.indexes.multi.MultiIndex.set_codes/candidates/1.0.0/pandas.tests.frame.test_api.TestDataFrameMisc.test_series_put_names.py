def test_series_put_names(self, float_string_frame):
    series = float_string_frame._series
    for k, v in series.items():
        assert v.name == k