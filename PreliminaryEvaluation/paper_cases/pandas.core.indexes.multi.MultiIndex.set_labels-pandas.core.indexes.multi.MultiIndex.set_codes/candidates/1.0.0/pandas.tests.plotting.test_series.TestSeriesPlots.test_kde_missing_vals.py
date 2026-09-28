@pytest.mark.slow
@td.skip_if_no_scipy
def test_kde_missing_vals(self):
    s = Series(np.random.uniform(size=50))
    s[0] = np.nan
    axes = _check_plot_works(s.plot.kde)
    assert any(~np.isnan(axes.lines[0].get_xdata()))