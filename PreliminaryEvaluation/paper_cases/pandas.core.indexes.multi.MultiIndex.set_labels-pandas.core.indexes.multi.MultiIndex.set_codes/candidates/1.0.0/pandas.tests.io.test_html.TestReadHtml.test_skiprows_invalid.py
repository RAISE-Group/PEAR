def test_skiprows_invalid(self):
    with pytest.raises(TypeError, match='is not a valid type for skipping rows'):
        self.read_html(self.spam_data, '.*Water.*', skiprows='asdf')