def test_ts_line_lim(self):
    fig, ax = self.plt.subplots()
    ax = self.ts.plot(ax=ax)
    xmin, xmax = ax.get_xlim()
    lines = ax.get_lines()
    assert xmin <= lines[0].get_data(orig=False)[0][0]
    assert xmax >= lines[0].get_data(orig=False)[0][-1]
    tm.close()
    ax = self.ts.plot(secondary_y=True, ax=ax)
    xmin, xmax = ax.get_xlim()
    lines = ax.get_lines()
    assert xmin <= lines[0].get_data(orig=False)[0][0]
    assert xmax >= lines[0].get_data(orig=False)[0][-1]