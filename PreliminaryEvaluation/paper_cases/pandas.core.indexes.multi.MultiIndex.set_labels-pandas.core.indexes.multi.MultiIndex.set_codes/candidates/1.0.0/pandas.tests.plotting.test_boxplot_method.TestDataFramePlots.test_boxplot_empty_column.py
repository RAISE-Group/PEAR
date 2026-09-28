@pytest.mark.slow
def test_boxplot_empty_column(self):
    df = DataFrame(np.random.randn(20, 4))
    df.loc[:, 0] = np.nan
    _check_plot_works(df.boxplot, return_type='axes')