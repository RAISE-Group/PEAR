def test_constructor_list_of_iterators(self):
    result = DataFrame([iter(range(10)), iter(range(10))])
    expected = DataFrame([list(range(10)), list(range(10))])
    tm.assert_frame_equal(result, expected)