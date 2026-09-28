def test_frame_from_list_subclass(self):

    class List(list):
        pass
    expected = DataFrame([[1, 2, 3], [4, 5, 6]])
    result = DataFrame(List([List([1, 2, 3]), List([4, 5, 6])]))
    tm.assert_frame_equal(result, expected)