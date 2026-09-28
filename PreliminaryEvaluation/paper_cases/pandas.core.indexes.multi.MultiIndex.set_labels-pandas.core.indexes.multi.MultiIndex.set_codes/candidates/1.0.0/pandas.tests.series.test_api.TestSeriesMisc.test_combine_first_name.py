def test_combine_first_name(self, datetime_series):
    result = datetime_series.combine_first(datetime_series[:5])
    assert result.name == datetime_series.name