def test_get_filepath_or_buffer_with_buffer(self):
    input_buffer = StringIO()
    filepath_or_buffer, _, _, should_close = icom.get_filepath_or_buffer(input_buffer)
    assert filepath_or_buffer == input_buffer
    assert not should_close