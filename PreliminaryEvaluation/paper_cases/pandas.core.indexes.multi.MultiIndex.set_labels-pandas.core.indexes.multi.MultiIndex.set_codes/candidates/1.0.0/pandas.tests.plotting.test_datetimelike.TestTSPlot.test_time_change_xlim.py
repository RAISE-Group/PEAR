@pytest.mark.slow
def test_time_change_xlim(self):
    t = datetime(1, 1, 1, 3, 30, 0)
    deltas = np.random.randint(1, 20, 3).cumsum()
    ts = np.array([(t + timedelta(minutes=int(x))).time() for x in deltas])
    df = DataFrame({'a': np.random.randn(len(ts)), 'b': np.random.randn(len(ts))}, index=ts)
    fig, ax = self.plt.subplots()
    df.plot(ax=ax)
    ticks = ax.get_xticks()
    labels = ax.get_xticklabels()
    for t, l in zip(ticks, labels):
        m, s = divmod(int(t), 60)
        h, m = divmod(m, 60)
        rs = l.get_text()
        if len(rs) > 0:
            if s != 0:
                xp = time(h, m, s).strftime('%H:%M:%S')
            else:
                xp = time(h, m, s).strftime('%H:%M')
            assert xp == rs
    ax.set_xlim('1:30', '5:00')
    ticks = ax.get_xticks()
    labels = ax.get_xticklabels()
    for t, l in zip(ticks, labels):
        m, s = divmod(int(t), 60)
        h, m = divmod(m, 60)
        rs = l.get_text()
        if len(rs) > 0:
            if s != 0:
                xp = time(h, m, s).strftime('%H:%M:%S')
            else:
                xp = time(h, m, s).strftime('%H:%M')
            assert xp == rs