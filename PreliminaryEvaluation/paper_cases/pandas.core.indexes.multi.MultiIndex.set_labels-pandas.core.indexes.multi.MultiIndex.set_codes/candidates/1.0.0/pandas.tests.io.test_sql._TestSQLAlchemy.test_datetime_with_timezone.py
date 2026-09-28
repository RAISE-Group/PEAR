def test_datetime_with_timezone(self):

    def check(col):
        if is_datetime64_dtype(col.dtype):
            assert col[0] == Timestamp('2000-01-01 08:00:00')
            assert col[1] == Timestamp('2000-06-01 07:00:00')
        elif is_datetime64tz_dtype(col.dtype):
            assert str(col.dt.tz) == 'UTC'
            expected_data = [Timestamp('2000-01-01 08:00:00', tz='UTC'), Timestamp('2000-06-01 07:00:00', tz='UTC')]
            expected = Series(expected_data, name=col.name)
            tm.assert_series_equal(col, expected)
        else:
            raise AssertionError(f'DateCol loaded with incorrect type -> {col.dtype}')
    df = pd.read_sql_query('select * from types_test_data', self.conn)
    if not hasattr(df, 'DateColWithTz'):
        pytest.skip('no column with datetime with time zone')
    col = df.DateColWithTz
    assert is_datetime64tz_dtype(col.dtype)
    df = pd.read_sql_query('select * from types_test_data', self.conn, parse_dates=['DateColWithTz'])
    if not hasattr(df, 'DateColWithTz'):
        pytest.skip('no column with datetime with time zone')
    col = df.DateColWithTz
    assert is_datetime64tz_dtype(col.dtype)
    assert str(col.dt.tz) == 'UTC'
    check(df.DateColWithTz)
    df = pd.concat(list(pd.read_sql_query('select * from types_test_data', self.conn, chunksize=1)), ignore_index=True)
    col = df.DateColWithTz
    assert is_datetime64tz_dtype(col.dtype)
    assert str(col.dt.tz) == 'UTC'
    expected = sql.read_sql_table('types_test_data', self.conn)
    col = expected.DateColWithTz
    assert is_datetime64tz_dtype(col.dtype)
    tm.assert_series_equal(df.DateColWithTz, expected.DateColWithTz)
    df = sql.read_sql_table('types_test_data', self.conn)
    check(df.DateColWithTz)