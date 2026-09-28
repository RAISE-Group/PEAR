def test_constructor_list_of_derived_dicts(self):

    class CustomDict(dict):
        pass
    d = {'a': 1.5, 'b': 3}
    data_custom = [CustomDict(d)]
    data = [d]
    result_custom = DataFrame(data_custom)
    result = DataFrame(data)
    tm.assert_frame_equal(result, result_custom)