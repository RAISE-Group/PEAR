def test_get_filepath_or_buffer_with_path(self):
    filename = '~/sometest'
    filepath_or_buffer, _, _, should_close = icom.get_filepath_or_buffer(filename)
    assert filepath_or_buffer != filename
    assert os.path.isabs(filepath_or_buffer)
    assert os.path.expanduser(filename) == filepath_or_buffer
    assert not should_close