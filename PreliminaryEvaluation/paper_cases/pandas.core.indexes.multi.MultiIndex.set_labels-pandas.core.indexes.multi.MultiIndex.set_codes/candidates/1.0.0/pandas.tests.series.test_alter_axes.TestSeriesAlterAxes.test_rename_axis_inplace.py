def test_rename_axis_inplace(self, datetime_series):
    expected = datetime_series.rename_axis('foo')
    result = datetime_series
    no_return = result.rename_axis('foo', inplace=True)
    assert no_return is None
    tm.assert_series_equal(result, expected)