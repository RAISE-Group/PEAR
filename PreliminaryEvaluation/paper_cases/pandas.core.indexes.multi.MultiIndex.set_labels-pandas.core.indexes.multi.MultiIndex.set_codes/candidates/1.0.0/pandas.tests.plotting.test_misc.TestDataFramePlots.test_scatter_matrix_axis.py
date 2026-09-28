@td.skip_if_no_scipy
def test_scatter_matrix_axis(self):
    scatter_matrix = plotting.scatter_matrix
    with tm.RNGContext(42):
        df = DataFrame(randn(100, 3))
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(scatter_matrix, filterwarnings='always', frame=df, range_padding=0.1)
    axes0_labels = axes[0][0].yaxis.get_majorticklabels()
    expected = ['-2', '0', '2']
    self._check_text_labels(axes0_labels, expected)
    self._check_ticks_props(axes, xlabelsize=8, xrot=90, ylabelsize=8, yrot=0)
    df[0] = (df[0] - 2) / 3
    with tm.assert_produces_warning(UserWarning):
        axes = _check_plot_works(scatter_matrix, filterwarnings='always', frame=df, range_padding=0.1)
    axes0_labels = axes[0][0].yaxis.get_majorticklabels()
    expected = ['-1.0', '-0.5', '0.0']
    self._check_text_labels(axes0_labels, expected)
    self._check_ticks_props(axes, xlabelsize=8, xrot=90, ylabelsize=8, yrot=0)