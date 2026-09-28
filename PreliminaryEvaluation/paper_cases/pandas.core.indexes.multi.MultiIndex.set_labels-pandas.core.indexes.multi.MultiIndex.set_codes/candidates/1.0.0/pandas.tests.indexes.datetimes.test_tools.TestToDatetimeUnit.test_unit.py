@pytest.mark.parametrize('cache', [True, False])
def test_unit(self, cache):
    with pytest.raises(ValueError):
        to_datetime([1], unit='D', format='%Y%m%d', cache=cache)
    values = [11111111, 1, 1.0, iNaT, NaT, np.nan, 'NaT', '']
    result = to_datetime(values, unit='D', errors='ignore', cache=cache)
    expected = Index([11111111, Timestamp('1970-01-02'), Timestamp('1970-01-02'), NaT, NaT, NaT, NaT, NaT], dtype=object)
    tm.assert_index_equal(result, expected)
    result = to_datetime(values, unit='D', errors='coerce', cache=cache)
    expected = DatetimeIndex(['NaT', '1970-01-02', '1970-01-02', 'NaT', 'NaT', 'NaT', 'NaT', 'NaT'])
    tm.assert_index_equal(result, expected)
    with pytest.raises(tslib.OutOfBoundsDatetime):
        to_datetime(values, unit='D', errors='raise', cache=cache)
    values = [1420043460000, iNaT, NaT, np.nan, 'NaT']
    result = to_datetime(values, errors='ignore', unit='s', cache=cache)
    expected = Index([1420043460000, NaT, NaT, NaT, NaT], dtype=object)
    tm.assert_index_equal(result, expected)
    result = to_datetime(values, errors='coerce', unit='s', cache=cache)
    expected = DatetimeIndex(['NaT', 'NaT', 'NaT', 'NaT', 'NaT'])
    tm.assert_index_equal(result, expected)
    with pytest.raises(tslib.OutOfBoundsDatetime):
        to_datetime(values, errors='raise', unit='s', cache=cache)
    for val in ['foo', Timestamp('20130101')]:
        try:
            to_datetime(val, errors='raise', unit='s', cache=cache)
        except tslib.OutOfBoundsDatetime:
            raise AssertionError('incorrect exception raised')
        except ValueError:
            pass