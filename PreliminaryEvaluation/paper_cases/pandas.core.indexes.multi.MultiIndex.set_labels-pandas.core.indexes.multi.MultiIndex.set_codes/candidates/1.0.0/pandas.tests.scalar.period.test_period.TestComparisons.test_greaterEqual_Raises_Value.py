def test_greaterEqual_Raises_Value(self):
    with pytest.raises(IncompatibleFrequency):
        self.january1 >= self.day
    with pytest.raises(TypeError):
        print(self.january1 >= 1)