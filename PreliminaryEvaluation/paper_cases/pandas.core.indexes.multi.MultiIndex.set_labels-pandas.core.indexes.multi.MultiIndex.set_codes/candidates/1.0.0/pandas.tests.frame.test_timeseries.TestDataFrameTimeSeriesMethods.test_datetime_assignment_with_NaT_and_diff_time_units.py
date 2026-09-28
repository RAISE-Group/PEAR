def test_datetime_assignment_with_NaT_and_diff_time_units(self):
    data_ns = np.array([1, 'nat'], dtype='datetime64[ns]')
    result = pd.Series(data_ns).to_frame()
    result['new'] = data_ns
    expected = pd.DataFrame({0: [1, None], 'new': [1, None]}, dtype='datetime64[ns]')
    tm.assert_frame_equal(result, expected)
    data_s = np.array([1, 'nat'], dtype='datetime64[s]')
    result['new'] = data_s
    expected = pd.DataFrame({0: [1, None], 'new': [1000000000.0, None]}, dtype='datetime64[ns]')
    tm.assert_frame_equal(result, expected)