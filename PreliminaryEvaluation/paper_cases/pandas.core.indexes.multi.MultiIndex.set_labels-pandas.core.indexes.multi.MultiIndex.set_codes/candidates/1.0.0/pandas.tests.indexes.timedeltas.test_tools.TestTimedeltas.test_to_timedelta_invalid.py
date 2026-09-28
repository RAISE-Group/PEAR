def test_to_timedelta_invalid(self):
    msg = 'errors must be one of'
    with pytest.raises(ValueError, match=msg):
        to_timedelta(['foo'], errors='never')
    msg = 'invalid unit abbreviation: foo'
    with pytest.raises(ValueError, match=msg):
        to_timedelta([1, 2], unit='foo')
    with pytest.raises(ValueError, match=msg):
        to_timedelta(1, unit='foo')
    msg = 'Value must be Timedelta, string, integer, float, timedelta or convertible'
    with pytest.raises(ValueError, match=msg):
        to_timedelta(time(second=1))
    assert to_timedelta(time(second=1), errors='coerce') is pd.NaT
    msg = 'unit abbreviation w/o a number'
    with pytest.raises(ValueError, match=msg):
        to_timedelta(['foo', 'bar'])
    tm.assert_index_equal(TimedeltaIndex([pd.NaT, pd.NaT]), to_timedelta(['foo', 'bar'], errors='coerce'))
    tm.assert_index_equal(TimedeltaIndex(['1 day', pd.NaT, '1 min']), to_timedelta(['1 day', 'bar', '1 min'], errors='coerce'))
    invalid_data = 'apple'
    assert invalid_data == to_timedelta(invalid_data, errors='ignore')
    invalid_data = ['apple', '1 days']
    tm.assert_numpy_array_equal(np.array(invalid_data, dtype=object), to_timedelta(invalid_data, errors='ignore'))
    invalid_data = pd.Index(['apple', '1 days'])
    tm.assert_index_equal(invalid_data, to_timedelta(invalid_data, errors='ignore'))
    invalid_data = Series(['apple', '1 days'])
    tm.assert_series_equal(invalid_data, to_timedelta(invalid_data, errors='ignore'))