@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_types(self, cache):
    result = to_datetime('', cache=cache)
    assert result is NaT
    result = to_datetime(['', ''], cache=cache)
    assert isna(result).all()
    result = Timestamp(0)
    expected = to_datetime(0, cache=cache)
    assert result == expected
    expected = to_datetime(['2012'], cache=cache)[0]
    result = to_datetime('2012', cache=cache)
    assert result == expected
    array = ['20120101', '20120101 12:01:01']
    expected = list(to_datetime(array, cache=cache))
    result = [Timestamp(date_str) for date_str in array]
    tm.assert_almost_equal(result, expected)