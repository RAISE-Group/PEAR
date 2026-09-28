def test_constructor_data_aware_dtype_naive(self, tz_aware_fixture):
    tz = tz_aware_fixture
    result = DataFrame({'d': [pd.Timestamp('2019', tz=tz)]}, dtype='datetime64[ns]')
    expected = DataFrame({'d': [pd.Timestamp('2019')]})
    tm.assert_frame_equal(result, expected)