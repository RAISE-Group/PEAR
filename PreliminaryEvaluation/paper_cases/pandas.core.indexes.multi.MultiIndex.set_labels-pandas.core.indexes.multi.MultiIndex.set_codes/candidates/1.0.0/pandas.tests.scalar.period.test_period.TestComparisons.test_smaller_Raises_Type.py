def test_smaller_Raises_Type(self):
    with pytest.raises(TypeError):
        self.january1 < 1