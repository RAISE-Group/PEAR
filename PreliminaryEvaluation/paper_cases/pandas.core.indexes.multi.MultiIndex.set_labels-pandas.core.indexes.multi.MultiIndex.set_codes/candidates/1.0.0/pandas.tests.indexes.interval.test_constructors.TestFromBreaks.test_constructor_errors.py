def test_constructor_errors(self):
    data = Categorical(list('01234abcde'), ordered=True)
    msg = 'category, object, and string subtypes are not supported for IntervalIndex'
    with pytest.raises(TypeError, match=msg):
        IntervalIndex.from_breaks(data)