def test_ground_truth(self):
    skew = nanops.nanskew(self.samples)
    tm.assert_almost_equal(skew, self.actual_skew)