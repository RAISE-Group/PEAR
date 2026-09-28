def test_copy_name(self, datetime_series):
    result = datetime_series.copy()
    assert result.name == datetime_series.name