def test_bounds_with_different_units(self):
    out_of_bounds_dates = ('1677-09-21', '2262-04-12')
    time_units = ('D', 'h', 'm', 's', 'ms', 'us')
    for date_string in out_of_bounds_dates:
        for unit in time_units:
            dt64 = np.datetime64(date_string, unit)
            with pytest.raises(ValueError):
                Timestamp(dt64)
    in_bounds_dates = ('1677-09-23', '2262-04-11')
    for date_string in in_bounds_dates:
        for unit in time_units:
            dt64 = np.datetime64(date_string, unit)
            Timestamp(dt64)