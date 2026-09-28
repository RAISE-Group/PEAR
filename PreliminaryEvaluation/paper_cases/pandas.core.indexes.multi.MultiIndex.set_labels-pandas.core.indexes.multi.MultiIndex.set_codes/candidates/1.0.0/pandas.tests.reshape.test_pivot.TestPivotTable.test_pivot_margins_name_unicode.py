def test_pivot_margins_name_unicode(self):
    greek = 'Δοκιμή'
    frame = pd.DataFrame({'foo': [1, 2, 3]})
    table = pd.pivot_table(frame, index=['foo'], aggfunc=len, margins=True, margins_name=greek)
    index = pd.Index([1, 2, 3, greek], dtype='object', name='foo')
    expected = pd.DataFrame(index=index)
    tm.assert_frame_equal(table, expected)