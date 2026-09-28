def test_validate_bool_args(self):
    invalid_values = [1, 'True', [1, 2, 3], 5.0]
    bm1 = create_mgr('a,b,c: i8-1; d,e,f: i8-2')
    for value in invalid_values:
        with pytest.raises(ValueError):
            bm1.replace_list([1], [2], inplace=value)