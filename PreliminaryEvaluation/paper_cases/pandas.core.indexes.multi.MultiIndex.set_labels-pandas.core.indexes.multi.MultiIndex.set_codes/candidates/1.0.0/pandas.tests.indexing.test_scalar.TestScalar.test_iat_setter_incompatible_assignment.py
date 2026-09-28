def test_iat_setter_incompatible_assignment(self):
    result = DataFrame({'a': [0, 1], 'b': [4, 5]})
    result.iat[0, 0] = None
    expected = DataFrame({'a': [None, 1], 'b': [4, 5]})
    tm.assert_frame_equal(result, expected)