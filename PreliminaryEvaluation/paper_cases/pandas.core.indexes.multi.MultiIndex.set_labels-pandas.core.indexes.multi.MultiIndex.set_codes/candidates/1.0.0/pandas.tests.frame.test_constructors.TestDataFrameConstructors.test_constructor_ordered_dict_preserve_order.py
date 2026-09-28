def test_constructor_ordered_dict_preserve_order(self):
    expected = DataFrame([[2, 1]], columns=['b', 'a'])
    data = OrderedDict()
    data['b'] = [2]
    data['a'] = [1]
    result = DataFrame(data)
    tm.assert_frame_equal(result, expected)
    data = OrderedDict()
    data['b'] = 2
    data['a'] = 1
    result = DataFrame([data])
    tm.assert_frame_equal(result, expected)