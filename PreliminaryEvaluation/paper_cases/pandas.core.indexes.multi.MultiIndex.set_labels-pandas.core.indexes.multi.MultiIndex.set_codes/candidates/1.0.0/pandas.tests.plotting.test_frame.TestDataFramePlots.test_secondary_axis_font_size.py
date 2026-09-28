@pytest.mark.parametrize('method', ['line', 'barh', 'bar'])
def test_secondary_axis_font_size(self, method):
    df = pd.DataFrame(np.random.randn(15, 2), columns=list('AB')).assign(C=lambda df: df.B.cumsum()).assign(D=lambda df: df.C * 1.1)
    fontsize = 20
    sy = ['C', 'D']
    kwargs = dict(secondary_y=sy, fontsize=fontsize, mark_right=True)
    ax = getattr(df.plot, method)(**kwargs)
    self._check_ticks_props(axes=ax.right_ax, ylabelsize=fontsize)