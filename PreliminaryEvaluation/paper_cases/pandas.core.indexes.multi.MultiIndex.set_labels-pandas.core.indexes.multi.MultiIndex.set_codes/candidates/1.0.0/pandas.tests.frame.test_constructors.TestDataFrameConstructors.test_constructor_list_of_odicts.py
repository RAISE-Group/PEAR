def test_constructor_list_of_odicts(self):
    data = [OrderedDict([['a', 1.5], ['b', 3], ['c', 4], ['d', 6]]), OrderedDict([['a', 1.5], ['b', 3], ['d', 6]]), OrderedDict([['a', 1.5], ['d', 6]]), OrderedDict(), OrderedDict([['a', 1.5], ['b', 3], ['c', 4]]), OrderedDict([['b', 3], ['c', 4], ['d', 6]])]
    result = DataFrame(data)
    expected = DataFrame.from_dict(dict(zip(range(len(data)), data)), orient='index')
    tm.assert_frame_equal(result, expected.reindex(result.index))
    result = DataFrame([{}])
    expected = DataFrame(index=[0])
    tm.assert_frame_equal(result, expected)