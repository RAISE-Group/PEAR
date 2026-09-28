def test_constructor_dict_datetime64_index(self):
    dates_as_str = ['1984-02-19', '1988-11-06', '1989-12-03', '1990-03-15']
    values = [42544017.198965244, 1234565, 40512335.18195823, -1]

    def create_data(constructor):
        return dict(zip((constructor(x) for x in dates_as_str), values))
    data_datetime64 = create_data(np.datetime64)
    data_datetime = create_data(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    data_Timestamp = create_data(Timestamp)
    expected = Series(values, (Timestamp(x) for x in dates_as_str))
    result_datetime64 = Series(data_datetime64)
    result_datetime = Series(data_datetime)
    result_Timestamp = Series(data_Timestamp)
    tm.assert_series_equal(result_datetime64, expected)
    tm.assert_series_equal(result_datetime, expected)
    tm.assert_series_equal(result_Timestamp, expected)