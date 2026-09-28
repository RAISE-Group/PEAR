def test_bool_header_arg(self):
    for arg in [True, False]:
        with pytest.raises(TypeError):
            self.read_html(self.spam_data, header=arg)