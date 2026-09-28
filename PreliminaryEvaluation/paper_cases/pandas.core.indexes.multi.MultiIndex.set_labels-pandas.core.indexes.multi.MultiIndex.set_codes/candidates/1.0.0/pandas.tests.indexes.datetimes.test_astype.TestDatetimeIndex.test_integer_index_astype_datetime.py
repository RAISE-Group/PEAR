@pytest.mark.parametrize('tz, dtype', [['US/Pacific', 'datetime64[ns, US/Pacific]'], [None, 'datetime64[ns]']])
def test_integer_index_astype_datetime(self, tz, dtype):
    val = [pd.Timestamp('2018-01-01', tz=tz).value]
    result = pd.Index(val).astype(dtype)
    expected = pd.DatetimeIndex(['2018-01-01'], tz=tz)
    tm.assert_index_equal(result, expected)