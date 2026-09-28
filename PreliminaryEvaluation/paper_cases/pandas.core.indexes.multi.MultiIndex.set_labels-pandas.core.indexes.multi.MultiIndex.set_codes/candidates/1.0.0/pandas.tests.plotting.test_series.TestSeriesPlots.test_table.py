def test_table(self):
    _check_plot_works(self.series.plot, table=True)
    _check_plot_works(self.series.plot, table=self.series)