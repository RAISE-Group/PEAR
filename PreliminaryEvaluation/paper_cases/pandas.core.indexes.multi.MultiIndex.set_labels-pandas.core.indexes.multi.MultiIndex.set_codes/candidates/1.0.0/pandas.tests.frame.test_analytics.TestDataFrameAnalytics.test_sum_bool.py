def test_sum_bool(self, float_frame):
    bools = np.isnan(float_frame)
    bools.sum(1)
    bools.sum(0)