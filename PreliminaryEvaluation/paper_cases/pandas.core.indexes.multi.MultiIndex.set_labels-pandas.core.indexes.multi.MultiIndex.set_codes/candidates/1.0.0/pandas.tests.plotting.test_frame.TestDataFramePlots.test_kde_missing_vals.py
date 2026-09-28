@pytest.mark.slow
@td.skip_if_no_scipy
def test_kde_missing_vals(self):
    df = DataFrame(np.random.uniform(size=(100, 4)))
    df.loc[0, 0] = np.nan
    _check_plot_works(df.plot, kind='kde')