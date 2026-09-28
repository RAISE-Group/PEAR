def test_too_many_names(self):
    index = self.create_index()
    with pytest.raises(ValueError, match='^Length'):
        index.names = ['roger', 'harold']