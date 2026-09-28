@pytest.mark.parametrize('breaks', [tuple('0123456789'), list('abcdefghij'), np.array(list('abcdefghij'), dtype=object), np.array(list('abcdefghij'), dtype='<U1')])
def test_constructor_string(self, constructor, breaks):
    msg = 'category, object, and string subtypes are not supported for IntervalIndex'
    with pytest.raises(TypeError, match=msg):
        constructor(**self.get_kwargs_from_breaks(breaks))