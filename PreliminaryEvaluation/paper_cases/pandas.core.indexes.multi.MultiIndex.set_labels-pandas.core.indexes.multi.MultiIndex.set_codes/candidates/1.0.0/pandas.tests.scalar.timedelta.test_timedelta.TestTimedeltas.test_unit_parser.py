@pytest.mark.parametrize('units, np_unit', [(['W', 'w'], 'W'), (['D', 'd', 'days', 'day', 'Days', 'Day'], 'D'), (['m', 'minute', 'min', 'minutes', 't', 'Minute', 'Min', 'Minutes', 'T'], 'm'), (['s', 'seconds', 'sec', 'second', 'S', 'Seconds', 'Sec', 'Second'], 's'), (['ms', 'milliseconds', 'millisecond', 'milli', 'millis', 'l', 'MS', 'Milliseconds', 'Millisecond', 'Milli', 'Millis', 'L'], 'ms'), (['us', 'microseconds', 'microsecond', 'micro', 'micros', 'u', 'US', 'Microseconds', 'Microsecond', 'Micro', 'Micros', 'U'], 'us'), (['ns', 'nanoseconds', 'nanosecond', 'nano', 'nanos', 'n', 'NS', 'Nanoseconds', 'Nanosecond', 'Nano', 'Nanos', 'N'], 'ns')])
@pytest.mark.parametrize('wrapper', [np.array, list, pd.Index])
def test_unit_parser(self, units, np_unit, wrapper):
    for unit in units:
        expected = TimedeltaIndex([np.timedelta64(i, np_unit) for i in np.arange(5).tolist()])
        result = to_timedelta(wrapper(range(5)), unit=unit)
        tm.assert_index_equal(result, expected)
        result = TimedeltaIndex(wrapper(range(5)), unit=unit)
        tm.assert_index_equal(result, expected)
        if unit == 'M':
            expected = TimedeltaIndex([np.timedelta64(i, 'm') for i in np.arange(5).tolist()])
        str_repr = [f'{x}{unit}' for x in np.arange(5)]
        result = to_timedelta(wrapper(str_repr))
        tm.assert_index_equal(result, expected)
        result = TimedeltaIndex(wrapper(str_repr))
        tm.assert_index_equal(result, expected)
        expected = Timedelta(np.timedelta64(2, np_unit).astype('timedelta64[ns]'))
        result = to_timedelta(2, unit=unit)
        assert result == expected
        result = Timedelta(2, unit=unit)
        assert result == expected
        if unit == 'M':
            expected = Timedelta(np.timedelta64(2, 'm').astype('timedelta64[ns]'))
        result = to_timedelta(f'2{unit}')
        assert result == expected
        result = Timedelta(f'2{unit}')
        assert result == expected