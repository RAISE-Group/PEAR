def test_xs_view(self):
    dm = DataFrame(np.arange(20.0).reshape(4, 5), index=range(4), columns=range(5))
    dm.xs(2)[:] = 10
    assert (dm.xs(2) == 10).all()