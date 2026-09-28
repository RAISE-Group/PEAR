@pytest.mark.parametrize('tuples,lists', [((), []), ((), []), (((), ()), [(), ()]), (((), ()), [[], []]), (([], []), [[], []]), (([1, 2, 3], [4, 5, 6]), [[1, 2, 3], [4, 5, 6]])])
def test_constructor_tuple(self, tuples, lists):
    result = DataFrame(tuples)
    expected = DataFrame(lists)
    tm.assert_frame_equal(result, expected)