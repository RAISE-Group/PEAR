def test_append_preserve_name(self, datetime_series):
    result = datetime_series[:5].append(datetime_series[5:])
    assert result.name == datetime_series.name