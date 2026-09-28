def test_constructor_list_of_tuples(self):
    result = DataFrame({'A': [(1, 2), (3, 4)]})
    expected = DataFrame({'A': Series([(1, 2), (3, 4)])})
    tm.assert_frame_equal(result, expected)