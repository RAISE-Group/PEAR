def test_constructor_tuple_of_tuples(self):
    data = ((1, 1), (2, 2), (2, 3))
    s = Series(data)
    assert tuple(s) == data