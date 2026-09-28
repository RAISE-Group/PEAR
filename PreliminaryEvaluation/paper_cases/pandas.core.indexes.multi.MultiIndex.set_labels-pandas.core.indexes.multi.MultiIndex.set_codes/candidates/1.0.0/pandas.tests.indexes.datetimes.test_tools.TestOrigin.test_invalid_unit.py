def test_invalid_unit(self, units, julian_dates):
    if units != 'D':
        with pytest.raises(ValueError):
            pd.to_datetime(julian_dates, unit=units, origin='julian')