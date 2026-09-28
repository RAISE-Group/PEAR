@td.skip_if_not_us_locale
def test_guess_datetime_format_for_array(self):
    expected_format = '%Y-%m-%d %H:%M:%S.%f'
    dt_string = datetime(2011, 12, 30, 0, 0, 0).strftime(expected_format)
    test_arrays = [np.array([dt_string, dt_string, dt_string], dtype='O'), np.array([np.nan, np.nan, dt_string], dtype='O'), np.array([dt_string, 'random_string'], dtype='O')]
    for test_array in test_arrays:
        assert tools._guess_datetime_format_for_array(test_array) == expected_format
    format_for_string_of_nans = tools._guess_datetime_format_for_array(np.array([np.nan, np.nan, np.nan], dtype='O'))
    assert format_for_string_of_nans is None