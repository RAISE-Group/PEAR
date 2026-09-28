def test_constant_series(self):
    for val in [3075.2, 3075.3, 3075.5]:
        data = val * np.ones(300)
        skew = nanops.nanskew(data)
        assert skew == 0.0