def test_constructor_sequence_like(self):

    class DummyContainer(abc.Sequence):

        def __init__(self, lst):
            self._lst = lst

        def __getitem__(self, n):
            return self._lst.__getitem__(n)

        def __len__(self, n):
            return self._lst.__len__()
    lst_containers = [DummyContainer([1, 'a']), DummyContainer([2, 'b'])]
    columns = ['num', 'str']
    result = DataFrame(lst_containers, columns=columns)
    expected = DataFrame([[1, 'a'], [2, 'b']], columns=columns)
    tm.assert_frame_equal(result, expected, check_dtype=False)
    import array
    result = DataFrame({'A': array.array('i', range(10))})
    expected = DataFrame({'A': list(range(10))})
    tm.assert_frame_equal(result, expected, check_dtype=False)
    expected = DataFrame([list(range(10)), list(range(10))])
    result = DataFrame([array.array('i', range(10)), array.array('i', range(10))])
    tm.assert_frame_equal(result, expected, check_dtype=False)