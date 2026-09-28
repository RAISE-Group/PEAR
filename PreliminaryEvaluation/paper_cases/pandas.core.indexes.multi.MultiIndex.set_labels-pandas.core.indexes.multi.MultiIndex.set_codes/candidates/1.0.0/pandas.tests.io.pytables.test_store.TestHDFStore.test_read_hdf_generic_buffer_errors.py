def test_read_hdf_generic_buffer_errors(self):
    with pytest.raises(NotImplementedError):
        read_hdf(BytesIO(b''), 'df')