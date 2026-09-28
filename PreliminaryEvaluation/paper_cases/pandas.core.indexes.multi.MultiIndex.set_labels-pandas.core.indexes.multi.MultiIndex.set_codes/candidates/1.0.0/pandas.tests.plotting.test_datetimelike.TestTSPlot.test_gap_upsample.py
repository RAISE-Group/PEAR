@pytest.mark.slow
def test_gap_upsample(self):
    low = tm.makeTimeSeries()
    low[5:25] = np.nan
    _, ax = self.plt.subplots()
    low.plot(ax=ax)
    idxh = date_range(low.index[0], low.index[-1], freq='12h')
    s = Series(np.random.randn(len(idxh)), idxh)
    s.plot(secondary_y=True)
    lines = ax.get_lines()
    assert len(lines) == 1
    assert len(ax.right_ax.get_lines()) == 1
    line = lines[0]
    data = line.get_xydata()
    if self.mpl_ge_3_0_0 or not self.mpl_ge_2_2_3:
        data = np.ma.MaskedArray(data, mask=isna(data), fill_value=np.nan)
    assert isinstance(data, np.ma.core.MaskedArray)
    mask = data.mask
    assert mask[5:25, 1].all()