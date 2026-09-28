@pytest.mark.parametrize('index', [date_range('1/1/2000', periods=10), timedelta_range('1 day', periods=10), period_range('2000-Q1', periods=10, freq='Q')], ids=lambda x: type(x).__name__)
def test_constructor_cant_cast_datetimelike(self, index):
    msg = 'Cannot cast {}.*? to '.format(type(index).__name__.rstrip('Index'))
    with pytest.raises(TypeError, match=msg):
        Series(index, dtype=float)
    result = Series(index, dtype=np.int64)
    expected = Series(index.astype(np.int64))
    tm.assert_series_equal(result, expected)