@pytest.mark.parametrize('klass', [Index, DatetimeIndex])
@pytest.mark.parametrize('box', [np.array, partial(np.array, dtype=object), list])
@pytest.mark.parametrize('tz, dtype', [('US/Pacific', 'datetime64[ns, US/Pacific]'), (None, 'datetime64[ns]')])
def test_constructor_with_int_tz(self, klass, box, tz, dtype):
    ts = Timestamp('2018-01-01', tz=tz)
    result = klass(box([ts.value]), dtype=dtype)
    expected = klass([ts])
    assert result == expected