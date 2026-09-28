def test_arg_for_errors_in_astype_dictlist(self):
    df = pd.DataFrame([{'a': '1', 'b': '16.5%', 'c': 'test'}, {'a': '2.2', 'b': '15.3', 'c': 'another_test'}])
    expected = pd.DataFrame([{'a': 1.0, 'b': '16.5%', 'c': 'test'}, {'a': 2.2, 'b': '15.3', 'c': 'another_test'}])
    type_dict = {'a': 'float64', 'b': 'float64', 'c': 'object'}
    result = df.astype(dtype=type_dict, errors='ignore')
    tm.assert_frame_equal(result, expected)