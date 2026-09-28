def test_replace_with_dict_with_bool_keys(self):
    s = pd.Series([True, False, True])
    with pytest.raises(TypeError, match='Cannot compare types .+'):
        s.replace({'asdf': 'asdb', True: 'yes'})