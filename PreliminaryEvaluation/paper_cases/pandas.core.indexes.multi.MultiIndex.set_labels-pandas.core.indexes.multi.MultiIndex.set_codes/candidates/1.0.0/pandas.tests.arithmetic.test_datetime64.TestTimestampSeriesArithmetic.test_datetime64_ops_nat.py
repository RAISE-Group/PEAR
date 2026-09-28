def test_datetime64_ops_nat(self):
    datetime_series = Series([NaT, Timestamp('19900315')])
    nat_series_dtype_timestamp = Series([NaT, NaT], dtype='datetime64[ns]')
    single_nat_dtype_datetime = Series([NaT], dtype='datetime64[ns]')
    tm.assert_series_equal(-NaT + datetime_series, nat_series_dtype_timestamp)
    msg = 'Unary negative expects'
    with pytest.raises(TypeError, match=msg):
        -single_nat_dtype_datetime + datetime_series
    tm.assert_series_equal(-NaT + nat_series_dtype_timestamp, nat_series_dtype_timestamp)
    with pytest.raises(TypeError, match=msg):
        -single_nat_dtype_datetime + nat_series_dtype_timestamp
    tm.assert_series_equal(nat_series_dtype_timestamp + NaT, nat_series_dtype_timestamp)
    tm.assert_series_equal(NaT + nat_series_dtype_timestamp, nat_series_dtype_timestamp)
    tm.assert_series_equal(nat_series_dtype_timestamp + NaT, nat_series_dtype_timestamp)
    tm.assert_series_equal(NaT + nat_series_dtype_timestamp, nat_series_dtype_timestamp)