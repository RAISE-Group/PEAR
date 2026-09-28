@pytest.mark.parametrize('names', [('foo', None, None), ('baz', 'bar', None), ('bar', 'bar', 'bar')])
@pytest.mark.parametrize('tz', [None, 'America/Chicago'])
def test_dti_add_series(self, tz, names):
    index = DatetimeIndex(['2016-06-28 05:30', '2016-06-28 05:31'], tz=tz, name=names[0])
    ser = Series([Timedelta(seconds=5)] * 2, index=index, name=names[1])
    expected = Series(index + Timedelta(seconds=5), index=index, name=names[2])
    expected.name = names[2]
    assert expected.dtype == index.dtype
    result = ser + index
    tm.assert_series_equal(result, expected)
    result2 = index + ser
    tm.assert_series_equal(result2, expected)
    expected = index + Timedelta(seconds=5)
    result3 = ser.values + index
    tm.assert_index_equal(result3, expected)
    result4 = index + ser.values
    tm.assert_index_equal(result4, expected)