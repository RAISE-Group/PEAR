def test_wrong_number_names(self, indices):
    with pytest.raises(ValueError, match='^Length'):
        indices.names = ['apple', 'banana', 'carrot']