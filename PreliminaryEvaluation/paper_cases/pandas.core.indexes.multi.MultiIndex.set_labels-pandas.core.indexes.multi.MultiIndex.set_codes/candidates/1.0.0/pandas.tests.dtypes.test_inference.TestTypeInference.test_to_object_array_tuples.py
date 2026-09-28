def test_to_object_array_tuples(self):
    r = (5, 6)
    values = [r]
    lib.to_object_array_tuples(values)
    record = namedtuple('record', 'x y')
    r = record(5, 6)
    values = [r]
    lib.to_object_array_tuples(values)