def test_constructor_wrong_kwargs(self):
    with pytest.raises(TypeError, match="Unexpected keyword arguments {'foo'}"):
        Index([], foo='bar')