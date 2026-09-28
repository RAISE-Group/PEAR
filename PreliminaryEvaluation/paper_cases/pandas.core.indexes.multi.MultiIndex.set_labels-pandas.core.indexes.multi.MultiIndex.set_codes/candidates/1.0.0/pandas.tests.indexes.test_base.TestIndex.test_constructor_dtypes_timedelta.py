@pytest.mark.parametrize('attr', ['values', 'asi8'])
@pytest.mark.parametrize('klass', [pd.Index, pd.TimedeltaIndex])
def test_constructor_dtypes_timedelta(self, attr, klass):
    index = pd.timedelta_range('1 days', periods=5)
    dtype = index.dtype
    values = getattr(index, attr)
    result = klass(values, dtype=dtype)
    tm.assert_index_equal(result, index)
    result = klass(list(values), dtype=dtype)
    tm.assert_index_equal(result, index)