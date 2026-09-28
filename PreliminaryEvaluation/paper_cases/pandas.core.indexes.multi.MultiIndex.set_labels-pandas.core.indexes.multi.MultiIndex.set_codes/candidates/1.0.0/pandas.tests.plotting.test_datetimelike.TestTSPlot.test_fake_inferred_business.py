def test_fake_inferred_business(self):
    _, ax = self.plt.subplots()
    rng = date_range('2001-1-1', '2001-1-10')
    ts = Series(range(len(rng)), index=rng)
    ts = ts[:3].append(ts[5:])
    ts.plot(ax=ax)
    assert not hasattr(ax, 'freq')