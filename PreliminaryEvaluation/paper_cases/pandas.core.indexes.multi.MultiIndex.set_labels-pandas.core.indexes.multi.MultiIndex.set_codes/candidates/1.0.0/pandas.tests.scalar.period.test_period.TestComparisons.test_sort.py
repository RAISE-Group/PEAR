def test_sort(self):
    periods = [self.march, self.january1, self.february]
    correctPeriods = [self.january1, self.february, self.march]
    assert sorted(periods) == correctPeriods