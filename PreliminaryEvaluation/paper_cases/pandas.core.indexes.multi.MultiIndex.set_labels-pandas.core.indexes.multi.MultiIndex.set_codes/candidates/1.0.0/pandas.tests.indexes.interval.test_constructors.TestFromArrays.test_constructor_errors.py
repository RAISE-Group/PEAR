def test_constructor_errors(self):
    data = Categorical(list('01234abcde'), ordered=True)
    msg = 'category, object, and string subtypes are not supported for IntervalIndex'
    with pytest.raises(TypeError, match=msg):
        IntervalIndex.from_arrays(data[:-1], data[1:])
    left = [0, 1, 2]
    right = [2, 3]
    msg = 'left and right must have the same length'
    with pytest.raises(ValueError, match=msg):
        IntervalIndex.from_arrays(left, right)