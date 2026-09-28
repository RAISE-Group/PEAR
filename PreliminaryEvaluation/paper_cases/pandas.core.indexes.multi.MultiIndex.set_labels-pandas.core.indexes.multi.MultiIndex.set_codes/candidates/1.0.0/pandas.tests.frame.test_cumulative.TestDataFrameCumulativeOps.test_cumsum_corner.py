def test_cumsum_corner(self):
    dm = DataFrame(np.arange(20).reshape(4, 5), index=range(4), columns=range(5))
    result = dm.cumsum()