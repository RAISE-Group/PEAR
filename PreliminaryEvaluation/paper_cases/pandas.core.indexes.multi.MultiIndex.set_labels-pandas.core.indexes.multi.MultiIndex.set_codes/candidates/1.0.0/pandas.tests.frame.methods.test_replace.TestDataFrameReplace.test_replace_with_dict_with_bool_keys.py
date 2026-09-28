def test_replace_with_dict_with_bool_keys(self):
    df = DataFrame({0: [True, False], 1: [False, True]})
    with pytest.raises(TypeError, match='Cannot compare types .+'):
        df.replace({'asdf': 'asdb', True: 'yes'})