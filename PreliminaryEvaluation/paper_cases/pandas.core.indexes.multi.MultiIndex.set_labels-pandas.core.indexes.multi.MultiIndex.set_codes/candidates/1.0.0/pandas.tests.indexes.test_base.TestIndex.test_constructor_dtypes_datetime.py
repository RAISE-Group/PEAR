@pytest.mark.parametrize('attr', ['values', 'asi8'])
@pytest.mark.parametrize('klass', [pd.Index, pd.DatetimeIndex])
def test_constructor_dtypes_datetime(self, tz_naive_fixture, attr, klass):
    index = pd.date_range('2011-01-01', periods=5)
    arg = getattr(index, attr)
    index = index.tz_localize(tz_naive_fixture)
    dtype = index.dtype
    if attr == 'asi8':
        result = pd.DatetimeIndex(arg).tz_localize(tz_naive_fixture)
    else:
        result = klass(arg, tz=tz_naive_fixture)
    tm.assert_index_equal(result, index)
    if attr == 'asi8':
        result = pd.DatetimeIndex(arg).astype(dtype)
    else:
        result = klass(arg, dtype=dtype)
    tm.assert_index_equal(result, index)
    if attr == 'asi8':
        result = pd.DatetimeIndex(list(arg)).tz_localize(tz_naive_fixture)
    else:
        result = klass(list(arg), tz=tz_naive_fixture)
    tm.assert_index_equal(result, index)
    if attr == 'asi8':
        result = pd.DatetimeIndex(list(arg)).astype(dtype)
    else:
        result = klass(list(arg), dtype=dtype)
    tm.assert_index_equal(result, index)