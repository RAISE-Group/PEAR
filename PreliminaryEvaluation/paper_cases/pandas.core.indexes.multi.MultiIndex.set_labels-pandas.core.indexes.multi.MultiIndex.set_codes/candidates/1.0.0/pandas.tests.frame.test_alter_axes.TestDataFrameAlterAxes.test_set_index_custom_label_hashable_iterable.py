def test_set_index_custom_label_hashable_iterable(self):

    class Thing(frozenset):

        def __repr__(self) -> str:
            tmp = sorted(self)
            return 'frozenset({{{}}})'.format(', '.join(map(repr, tmp)))
    thing1 = Thing(['One', 'red'])
    thing2 = Thing(['Two', 'blue'])
    df = DataFrame({thing1: [0, 1], thing2: [2, 3]})
    expected = DataFrame({thing1: [0, 1]}, index=Index([2, 3], name=thing2))
    result = df.set_index(thing2)
    tm.assert_frame_equal(result, expected)
    result = df.set_index([thing2])
    tm.assert_frame_equal(result, expected)
    thing3 = Thing(['Three', 'pink'])
    msg = "frozenset\\(\\{'Three', 'pink'\\}\\)"
    with pytest.raises(KeyError, match=msg):
        df.set_index(thing3)
    with pytest.raises(KeyError, match=msg):
        df.set_index([thing3])