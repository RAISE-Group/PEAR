def test_non_interable_record_path_errors(self):
    test_input = {'state': 'Texas', 'info': 1}
    test_path = 'info'
    msg = f'{test_input} has non iterable value 1 for path {test_path}. Must be iterable or null.'
    with pytest.raises(TypeError, match=msg):
        json_normalize([test_input], record_path=[test_path])