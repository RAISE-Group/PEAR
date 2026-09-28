def test_index_constructor_with_numpy_object_array_and_timestamp_tz_with_nan(self):
    result = Index(np.array([Timestamp('2019', tz='UTC'), np.nan], dtype=object))
    expected = DatetimeIndex([Timestamp('2019', tz='UTC'), pd.NaT])
    tm.assert_index_equal(result, expected)