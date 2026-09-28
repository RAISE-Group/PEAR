def test_scalarop_preserve_name(self, datetime_series):
    result = datetime_series * 2
    assert result.name == datetime_series.name