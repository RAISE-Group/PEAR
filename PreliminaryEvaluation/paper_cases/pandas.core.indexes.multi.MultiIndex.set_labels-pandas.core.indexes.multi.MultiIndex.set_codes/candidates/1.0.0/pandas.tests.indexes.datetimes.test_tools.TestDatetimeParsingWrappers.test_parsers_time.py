@td.skip_if_has_locale
def test_parsers_time(self):
    strings = ['14:15', '1415', '2:15pm', '0215pm', '14:15:00', '141500', '2:15:00pm', '021500pm', time(14, 15)]
    expected = time(14, 15)
    for time_string in strings:
        assert tools.to_time(time_string) == expected
    new_string = '14.15'
    msg = "Cannot convert arg \\['14\\.15'\\] to a time"
    with pytest.raises(ValueError, match=msg):
        tools.to_time(new_string)
    assert tools.to_time(new_string, format='%H.%M') == expected
    arg = ['14:15', '20:20']
    expected_arr = [time(14, 15), time(20, 20)]
    assert tools.to_time(arg) == expected_arr
    assert tools.to_time(arg, format='%H:%M') == expected_arr
    assert tools.to_time(arg, infer_time_format=True) == expected_arr
    assert tools.to_time(arg, format='%I:%M%p', errors='coerce') == [None, None]
    res = tools.to_time(arg, format='%I:%M%p', errors='ignore')
    tm.assert_numpy_array_equal(res, np.array(arg, dtype=np.object_))
    with pytest.raises(ValueError):
        tools.to_time(arg, format='%I:%M%p', errors='raise')
    tm.assert_series_equal(tools.to_time(Series(arg, name='test')), Series(expected_arr, name='test'))
    res = tools.to_time(np.array(arg))
    assert isinstance(res, list)
    assert res == expected_arr