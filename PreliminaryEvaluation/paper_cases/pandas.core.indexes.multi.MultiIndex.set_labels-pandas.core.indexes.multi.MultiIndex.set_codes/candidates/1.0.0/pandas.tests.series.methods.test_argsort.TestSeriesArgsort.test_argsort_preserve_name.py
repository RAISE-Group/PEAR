def test_argsort_preserve_name(self, datetime_series):
    result = datetime_series.argsort()
    assert result.name == datetime_series.name