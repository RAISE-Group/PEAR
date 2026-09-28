def test_construction_with_nat_and_tzlocal(self):
    tz = dateutil.tz.tzlocal()
    result = DatetimeIndex(['2018', 'NaT'], tz=tz)
    expected = DatetimeIndex([Timestamp('2018', tz=tz), pd.NaT])
    tm.assert_index_equal(result, expected)