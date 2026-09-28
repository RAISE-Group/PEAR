def test_integer_values_and_tz_interpreted_as_utc(self):
    val = np.datetime64('2000-01-01 00:00:00', 'ns')
    values = np.array([val.view('i8')])
    result = DatetimeIndex(values).tz_localize('US/Central')
    expected = pd.DatetimeIndex(['2000-01-01T00:00:00'], tz='US/Central')
    tm.assert_index_equal(result, expected)
    with tm.assert_produces_warning(None):
        result = DatetimeIndex(values, tz='UTC')
    expected = pd.DatetimeIndex(['2000-01-01T00:00:00'], tz='US/Central')