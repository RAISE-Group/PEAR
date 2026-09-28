def test_irregular_datetime(self):
    rng = date_range('1/1/2000', '3/1/2000')
    rng = rng[[0, 1, 2, 3, 5, 9, 10, 11, 12]]
    ser = Series(randn(len(rng)), rng)
    _, ax = self.plt.subplots()
    ax = ser.plot(ax=ax)
    xp = datetime(1999, 1, 1).toordinal()
    ax.set_xlim('1/1/1999', '1/1/2001')
    assert xp == ax.get_xlim()[0]