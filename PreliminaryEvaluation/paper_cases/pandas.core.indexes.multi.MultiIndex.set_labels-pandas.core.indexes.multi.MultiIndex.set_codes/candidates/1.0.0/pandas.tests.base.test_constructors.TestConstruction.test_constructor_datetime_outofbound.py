@pytest.mark.parametrize('klass', [Series, lambda x, **kwargs: DataFrame({'a': x}, **kwargs)['a'], pytest.param(lambda x, **kwargs: DataFrame(x, **kwargs)[0], marks=pytest.mark.xfail), Index])
@pytest.mark.parametrize('a', [np.array(['2263-01-01'], dtype='datetime64[D]'), np.array([datetime(2263, 1, 1)], dtype=object), np.array([np.datetime64('2263-01-01', 'D')], dtype=object), np.array(['2263-01-01'], dtype=object)], ids=['datetime64[D]', 'object-datetime.datetime', 'object-numpy-scalar', 'object-string'])
def test_constructor_datetime_outofbound(self, a, klass):
    if a.dtype.kind == 'M':
        with pytest.raises(pd.errors.OutOfBoundsDatetime):
            klass(a)
    else:
        result = klass(a)
        assert result.dtype == 'object'
        tm.assert_numpy_array_equal(result.to_numpy(), a)
    with pytest.raises(pd.errors.OutOfBoundsDatetime):
        klass(a, dtype='datetime64[ns]')