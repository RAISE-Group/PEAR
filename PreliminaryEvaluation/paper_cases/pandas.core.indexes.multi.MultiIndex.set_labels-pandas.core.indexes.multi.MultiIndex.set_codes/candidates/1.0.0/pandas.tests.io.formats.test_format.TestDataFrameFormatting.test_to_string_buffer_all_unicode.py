def test_to_string_buffer_all_unicode(self):
    buf = StringIO()
    empty = DataFrame({'c/σ': Series(dtype=object)})
    nonempty = DataFrame({'c/σ': Series([1, 2, 3])})
    print(empty, file=buf)
    print(nonempty, file=buf)
    buf.getvalue()