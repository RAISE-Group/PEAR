def test_constructor_coverage(self):
    rng = date_range('1/1/2000', periods=10.5)
    exp = date_range('1/1/2000', periods=10)
    tm.assert_index_equal(rng, exp)
    msg = 'periods must be a number, got foo'
    with pytest.raises(TypeError, match=msg):
        date_range(start='1/1/2000', periods='foo', freq='D')
    with pytest.raises(TypeError):
        DatetimeIndex('1/1/2000')
    gen = (datetime(2000, 1, 1) + timedelta(i) for i in range(10))
    result = DatetimeIndex(gen)
    expected = DatetimeIndex([datetime(2000, 1, 1) + timedelta(i) for i in range(10)])
    tm.assert_index_equal(result, expected)
    strings = np.array(['2000-01-01', '2000-01-02', '2000-01-03'])
    result = DatetimeIndex(strings)
    expected = DatetimeIndex(strings.astype('O'))
    tm.assert_index_equal(result, expected)
    from_ints = DatetimeIndex(expected.asi8)
    tm.assert_index_equal(from_ints, expected)
    strings = np.array(['2000-01-01', '2000-01-02', 'NaT'])
    result = DatetimeIndex(strings)
    expected = DatetimeIndex(strings.astype('O'))
    tm.assert_index_equal(result, expected)
    from_ints = DatetimeIndex(expected.asi8)
    tm.assert_index_equal(from_ints, expected)
    msg = 'Inferred frequency None from passed values does not conform to passed frequency D'
    with pytest.raises(ValueError, match=msg):
        DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-04'], freq='D')
    msg = 'Of the four parameters: start, end, periods, and freq, exactly three must be specified'
    with pytest.raises(ValueError, match=msg):
        date_range(start='2011-01-01', freq='b')
    with pytest.raises(ValueError, match=msg):
        date_range(end='2011-01-01', freq='B')
    with pytest.raises(ValueError, match=msg):
        date_range(periods=10, freq='D')