@pytest.mark.slow
def test_line_plot_period_frame(self):
    for df in self.period_df:
        _check_plot_works(df.plot, df.index.freq)