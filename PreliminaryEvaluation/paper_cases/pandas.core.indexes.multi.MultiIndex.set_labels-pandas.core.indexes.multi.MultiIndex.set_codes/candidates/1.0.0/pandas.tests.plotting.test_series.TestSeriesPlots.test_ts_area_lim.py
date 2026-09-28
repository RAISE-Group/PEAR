def test_ts_area_lim(self):
    _, ax = self.plt.subplots()
    ax = self.ts.plot.area(stacked=False, ax=ax)
    xmin, xmax = ax.get_xlim()
    line = ax.get_lines()[0].get_data(orig=False)[0]
    assert xmin <= line[0]
    assert xmax >= line[-1]
    tm.close()
    _, ax = self.plt.subplots()
    ax = self.ts.plot.area(stacked=False, x_compat=True, ax=ax)
    xmin, xmax = ax.get_xlim()
    line = ax.get_lines()[0].get_data(orig=False)[0]
    assert xmin <= line[0]
    assert xmax >= line[-1]
    tm.close()
    tz_ts = self.ts.copy()
    tz_ts.index = tz_ts.tz_localize('GMT').tz_convert('CET')
    _, ax = self.plt.subplots()
    ax = tz_ts.plot.area(stacked=False, x_compat=True, ax=ax)
    xmin, xmax = ax.get_xlim()
    line = ax.get_lines()[0].get_data(orig=False)[0]
    assert xmin <= line[0]
    assert xmax >= line[-1]
    tm.close()
    _, ax = self.plt.subplots()
    ax = tz_ts.plot.area(stacked=False, secondary_y=True, ax=ax)
    xmin, xmax = ax.get_xlim()
    line = ax.get_lines()[0].get_data(orig=False)[0]
    assert xmin <= line[0]
    assert xmax >= line[-1]