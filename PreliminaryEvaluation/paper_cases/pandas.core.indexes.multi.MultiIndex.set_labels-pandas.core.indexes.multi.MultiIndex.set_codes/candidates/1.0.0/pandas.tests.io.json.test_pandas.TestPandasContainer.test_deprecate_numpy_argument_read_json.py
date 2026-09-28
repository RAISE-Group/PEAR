def test_deprecate_numpy_argument_read_json(self):
    expected = DataFrame([1, 2, 3])
    with tm.assert_produces_warning(FutureWarning):
        result = read_json(expected.to_json(), numpy=True)
        tm.assert_frame_equal(result, expected)