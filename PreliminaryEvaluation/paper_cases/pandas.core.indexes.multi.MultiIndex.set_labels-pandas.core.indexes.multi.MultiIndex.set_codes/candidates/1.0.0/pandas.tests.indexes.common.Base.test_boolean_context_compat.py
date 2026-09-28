def test_boolean_context_compat(self):
    idx = self.create_index()
    with pytest.raises(ValueError, match='The truth value of a'):
        if idx:
            pass