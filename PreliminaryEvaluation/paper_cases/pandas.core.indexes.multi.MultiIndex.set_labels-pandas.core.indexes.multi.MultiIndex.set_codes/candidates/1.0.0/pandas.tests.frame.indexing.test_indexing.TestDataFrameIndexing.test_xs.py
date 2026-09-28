def test_xs(self, float_frame, datetime_frame):
    idx = float_frame.index[5]
    xs = float_frame.xs(idx)
    for item, value in xs.items():
        if np.isnan(value):
            assert np.isnan(float_frame[item][idx])
        else:
            assert value == float_frame[item][idx]
    test_data = {'A': {'1': 1, '2': 2}, 'B': {'1': '1', '2': '2', '3': '3'}}
    frame = DataFrame(test_data)
    xs = frame.xs('1')
    assert xs.dtype == np.object_
    assert xs['A'] == 1
    assert xs['B'] == '1'
    with pytest.raises(KeyError, match=re.escape("Timestamp('1999-12-31 00:00:00', freq='B')")):
        datetime_frame.xs(datetime_frame.index[0] - BDay())
    series = float_frame.xs('A', axis=1)
    expected = float_frame['A']
    tm.assert_series_equal(series, expected)
    series = float_frame.xs('A', axis=1)
    series[:] = 5
    assert (expected == 5).all()