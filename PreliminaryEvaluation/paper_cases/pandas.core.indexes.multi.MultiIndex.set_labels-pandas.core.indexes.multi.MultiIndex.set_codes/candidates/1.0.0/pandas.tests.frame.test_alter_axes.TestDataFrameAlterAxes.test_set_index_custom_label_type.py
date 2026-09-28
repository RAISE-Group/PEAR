def test_set_index_custom_label_type(self):

    class Thing:

        def __init__(self, name, color):
            self.name = name
            self.color = color

        def __str__(self) -> str:
            return f'<Thing {repr(self.name)}>'
        __repr__ = __str__
    thing1 = Thing('One', 'red')
    thing2 = Thing('Two', 'blue')
    df = DataFrame({thing1: [0, 1], thing2: [2, 3]})
    expected = DataFrame({thing1: [0, 1]}, index=Index([2, 3], name=thing2))
    result = df.set_index(thing2)
    tm.assert_frame_equal(result, expected)
    result = df.set_index([thing2])
    tm.assert_frame_equal(result, expected)
    thing3 = Thing('Three', 'pink')
    msg = "<Thing 'Three'>"
    with pytest.raises(KeyError, match=msg):
        df.set_index(thing3)
    with pytest.raises(KeyError, match=msg):
        df.set_index([thing3])