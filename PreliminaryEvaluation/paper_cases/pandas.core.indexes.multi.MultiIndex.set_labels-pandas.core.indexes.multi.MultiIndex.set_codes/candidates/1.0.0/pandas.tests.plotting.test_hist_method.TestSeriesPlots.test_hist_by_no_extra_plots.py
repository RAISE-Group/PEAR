@pytest.mark.slow
def test_hist_by_no_extra_plots(self):
    df = self.hist_df
    axes = df.height.hist(by=df.gender)
    assert len(self.plt.get_fignums()) == 1