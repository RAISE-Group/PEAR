@pytest.mark.slow
def test_hist_layout_with_by(self):
    df = self.hist_df
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.height.hist, by=df.gender, layout=(2, 1))
    self._check_axes_shape(axes, axes_num=2, layout=(2, 1))
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.height.hist, by=df.gender, layout=(3, -1))
    self._check_axes_shape(axes, axes_num=2, layout=(3, 1))
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.height.hist, by=df.category, layout=(4, 1))
    self._check_axes_shape(axes, axes_num=4, layout=(4, 1))
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.height.hist, by=df.category, layout=(2, -1))
    self._check_axes_shape(axes, axes_num=4, layout=(2, 2))
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.height.hist, by=df.category, layout=(3, -1))
    self._check_axes_shape(axes, axes_num=4, layout=(3, 2))
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.height.hist, by=df.category, layout=(-1, 4))
    self._check_axes_shape(axes, axes_num=4, layout=(1, 4))
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(df.height.hist, by=df.classroom, layout=(2, 2))
    self._check_axes_shape(axes, axes_num=3, layout=(2, 2))
    axes = df.height.hist(by=df.category, layout=(4, 2), figsize=(12, 7))
    self._check_axes_shape(axes, axes_num=4, layout=(4, 2), figsize=(12, 7))