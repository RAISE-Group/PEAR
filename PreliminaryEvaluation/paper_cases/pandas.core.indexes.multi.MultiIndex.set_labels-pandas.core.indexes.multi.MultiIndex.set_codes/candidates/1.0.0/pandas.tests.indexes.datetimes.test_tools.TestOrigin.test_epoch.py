def test_epoch(self, units, epochs, epoch_1960, units_from_epochs):
    expected = Series([pd.Timedelta(x, unit=units) + epoch_1960 for x in units_from_epochs])
    result = Series(pd.to_datetime(units_from_epochs, unit=units, origin=epochs))
    tm.assert_series_equal(result, expected)