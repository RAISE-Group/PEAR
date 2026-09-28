def test_set_name_attribute(self):
    s = Series([1, 2, 3])
    s2 = Series([1, 2, 3], name='bar')
    for name in [7, 7.0, 'name', datetime(2001, 1, 1), (1,), 'א']:
        s.name = name
        assert s.name == name
        s2.name = name
        assert s2.name == name