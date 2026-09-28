@pytest.mark.slow
def test_boxplot_return_type_none(self):
    result = self.hist_df.boxplot()
    assert isinstance(result, self.plt.Axes)