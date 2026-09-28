def test_ground_truth(self):
    kurt = nanops.nankurt(self.samples)
    tm.assert_almost_equal(kurt, self.actual_kurt)