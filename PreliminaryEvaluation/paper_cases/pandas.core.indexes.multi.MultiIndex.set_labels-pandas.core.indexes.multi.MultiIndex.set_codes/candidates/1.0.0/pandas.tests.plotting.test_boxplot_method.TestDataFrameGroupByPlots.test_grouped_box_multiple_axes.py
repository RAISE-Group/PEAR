@pytest.mark.slow
def test_grouped_box_multiple_axes(self):
    df = self.hist_df
    with tm.assert_produces_warning(UserWarning):
        fig, axes = self.plt.subplots(2, 2)
        df.groupby('category').boxplot(column='height', return_type='axes', ax=axes)
        self._check_axes_shape(self.plt.gcf().axes, axes_num=4, layout=(2, 2))
    fig, axes = self.plt.subplots(2, 3)
    with tm.assert_produces_warning(UserWarning):
        returned = df.boxplot(column=['height', 'weight', 'category'], by='gender', return_type='axes', ax=axes[0])
    returned = np.array(list(returned.values))
    self._check_axes_shape(returned, axes_num=3, layout=(1, 3))
    tm.assert_numpy_array_equal(returned, axes[0])
    assert returned[0].figure is fig
    with tm.assert_produces_warning(UserWarning):
        returned = df.groupby('classroom').boxplot(column=['height', 'weight', 'category'], return_type='axes', ax=axes[1])
    returned = np.array(list(returned.values))
    self._check_axes_shape(returned, axes_num=3, layout=(1, 3))
    tm.assert_numpy_array_equal(returned, axes[1])
    assert returned[0].figure is fig
    with pytest.raises(ValueError):
        fig, axes = self.plt.subplots(2, 3)
        with tm.assert_produces_warning(UserWarning):
            axes = df.groupby('classroom').boxplot(ax=axes)