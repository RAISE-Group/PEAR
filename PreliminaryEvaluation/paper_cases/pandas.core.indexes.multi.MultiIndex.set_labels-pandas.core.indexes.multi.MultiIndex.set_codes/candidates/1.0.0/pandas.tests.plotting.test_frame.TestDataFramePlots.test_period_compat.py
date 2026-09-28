def test_period_compat(self):
    df = DataFrame(np.random.rand(21, 2), index=bdate_range(datetime(2000, 1, 1), datetime(2000, 1, 31)), columns=['a', 'b'])
    df.plot()
    self.plt.axhline(y=0)
    tm.close()