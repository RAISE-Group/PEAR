def test_constructor_name_hashable(self):
    for n in [777, 777.0, 'name', datetime(2001, 11, 11), (1,), 'א']:
        for data in [[1, 2, 3], np.ones(3), {'a': 0, 'b': 1}]:
            s = Series(data, name=n)
            assert s.name == n