def test_convert_objects_no_conversion(self):
    mixed1 = DataFrame({'a': [1, 2, 3], 'b': [4.0, 5, 6], 'c': ['x', 'y', 'z']})
    mixed2 = mixed1._convert(datetime=True)
    tm.assert_frame_equal(mixed1, mixed2)