@pytest.mark.slow
def test_tight_layout(self):
    df = DataFrame(randn(100, 3))
    _check_plot_works(df.hist)
    self.plt.tight_layout()
    tm.close()