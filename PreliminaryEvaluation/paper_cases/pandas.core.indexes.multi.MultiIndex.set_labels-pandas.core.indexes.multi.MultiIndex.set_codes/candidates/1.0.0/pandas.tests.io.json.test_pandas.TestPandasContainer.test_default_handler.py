def test_default_handler(self):
    value = object()
    frame = DataFrame({'a': [7, value]})
    expected = DataFrame({'a': [7, str(value)]})
    result = pd.read_json(frame.to_json(default_handler=str))
    tm.assert_frame_equal(expected, result, check_index_type=False)