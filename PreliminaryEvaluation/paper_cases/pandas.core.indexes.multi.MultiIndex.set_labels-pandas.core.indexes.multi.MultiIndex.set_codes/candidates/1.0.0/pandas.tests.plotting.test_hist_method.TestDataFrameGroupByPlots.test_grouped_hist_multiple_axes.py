@pytest.mark.slow
def test_grouped_hist_multiple_axes(self):
    df = self.hist_df
    fig, axes = self.plt.subplots(2, 3)
    returned = df.hist(column=['height', 'weight', 'category'], ax=axes[0])
    self._check_axes_shape(returned, axes_num=3, layout=(1, 3))
    tm.assert_numpy_array_equal(returned, axes[0])
    assert returned[0].figure is fig
    returned = df.hist(by='classroom', ax=axes[1])
    self._check_axes_shape(returned, axes_num=3, layout=(1, 3))
    tm.assert_numpy_array_equal(returned, axes[1])
    assert returned[0].figure is fig
    with pytest.raises(ValueError):
        fig, axes = self.plt.subplots(2, 3)
        axes = df.hist(column='height', ax=axes)