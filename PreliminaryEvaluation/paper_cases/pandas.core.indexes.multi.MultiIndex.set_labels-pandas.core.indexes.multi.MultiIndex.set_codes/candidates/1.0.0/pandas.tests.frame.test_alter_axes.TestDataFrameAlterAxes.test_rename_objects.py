def test_rename_objects(self, float_string_frame):
    renamed = float_string_frame.rename(columns=str.upper)
    assert 'FOO' in renamed
    assert 'foo' not in renamed