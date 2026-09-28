def test_smallerEqual_Raises_Value(self):
    with pytest.raises(IncompatibleFrequency):
        self.january1 <= self.day