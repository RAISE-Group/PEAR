@pytest.mark.slow
def test_line_plot_datetime_frame(self):
    for df in self.datetime_df:
        freq = df.index.to_period(df.index.freq.rule_code).freq
        _check_plot_works(df.plot, freq)