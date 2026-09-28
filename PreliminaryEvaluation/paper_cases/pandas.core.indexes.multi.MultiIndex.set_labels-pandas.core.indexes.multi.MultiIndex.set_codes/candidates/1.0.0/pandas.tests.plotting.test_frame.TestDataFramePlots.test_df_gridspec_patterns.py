@pytest.mark.slow
def test_df_gridspec_patterns(self):
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    ts = Series(np.random.randn(10), index=date_range('1/1/2000', periods=10))
    df = DataFrame(np.random.randn(10, 2), index=ts.index, columns=list('AB'))

    def _get_vertical_grid():
        gs = gridspec.GridSpec(3, 1)
        fig = plt.figure()
        ax1 = fig.add_subplot(gs[:2, :])
        ax2 = fig.add_subplot(gs[2, :])
        return (ax1, ax2)

    def _get_horizontal_grid():
        gs = gridspec.GridSpec(1, 3)
        fig = plt.figure()
        ax1 = fig.add_subplot(gs[:, :2])
        ax2 = fig.add_subplot(gs[:, 2])
        return (ax1, ax2)
    for ax1, ax2 in [_get_vertical_grid(), _get_horizontal_grid()]:
        ax1 = ts.plot(ax=ax1)
        assert len(ax1.lines) == 1
        ax2 = df.plot(ax=ax2)
        assert len(ax2.lines) == 2
        for ax in [ax1, ax2]:
            self._check_visible(ax.get_yticklabels(), visible=True)
            self._check_visible(ax.get_xticklabels(), visible=True)
            self._check_visible(ax.get_xticklabels(minor=True), visible=True)
        tm.close()
    for ax1, ax2 in [_get_vertical_grid(), _get_horizontal_grid()]:
        axes = df.plot(subplots=True, ax=[ax1, ax2])
        assert len(ax1.lines) == 1
        assert len(ax2.lines) == 1
        for ax in axes:
            self._check_visible(ax.get_yticklabels(), visible=True)
            self._check_visible(ax.get_xticklabels(), visible=True)
            self._check_visible(ax.get_xticklabels(minor=True), visible=True)
        tm.close()
    ax1, ax2 = _get_vertical_grid()
    with tm.assert_produces_warning(UserWarning):
        axes = df.plot(subplots=True, ax=[ax1, ax2], sharex=True, sharey=True)
    assert len(axes[0].lines) == 1
    assert len(axes[1].lines) == 1
    for ax in [ax1, ax2]:
        self._check_visible(ax.get_yticklabels(), visible=True)
    self._check_visible(axes[0].get_xticklabels(), visible=False)
    self._check_visible(axes[0].get_xticklabels(minor=True), visible=False)
    self._check_visible(axes[1].get_xticklabels(), visible=True)
    self._check_visible(axes[1].get_xticklabels(minor=True), visible=True)
    tm.close()
    ax1, ax2 = _get_horizontal_grid()
    with tm.assert_produces_warning(UserWarning):
        axes = df.plot(subplots=True, ax=[ax1, ax2], sharex=True, sharey=True)
    assert len(axes[0].lines) == 1
    assert len(axes[1].lines) == 1
    self._check_visible(axes[0].get_yticklabels(), visible=True)
    self._check_visible(axes[1].get_yticklabels(), visible=False)
    for ax in [ax1, ax2]:
        self._check_visible(ax.get_xticklabels(), visible=True)
        self._check_visible(ax.get_xticklabels(minor=True), visible=True)
    tm.close()

    def _get_boxed_grid():
        gs = gridspec.GridSpec(3, 3)
        fig = plt.figure()
        ax1 = fig.add_subplot(gs[:2, :2])
        ax2 = fig.add_subplot(gs[:2, 2])
        ax3 = fig.add_subplot(gs[2, :2])
        ax4 = fig.add_subplot(gs[2, 2])
        return (ax1, ax2, ax3, ax4)
    axes = _get_boxed_grid()
    df = DataFrame(np.random.randn(10, 4), index=ts.index, columns=list('ABCD'))
    axes = df.plot(subplots=True, ax=axes)
    for ax in axes:
        assert len(ax.lines) == 1
        self._check_visible(ax.get_yticklabels(), visible=True)
        self._check_visible(ax.get_xticklabels(), visible=True)
        self._check_visible(ax.get_xticklabels(minor=True), visible=True)
    tm.close()
    axes = _get_boxed_grid()
    with tm.assert_produces_warning(UserWarning):
        axes = df.plot(subplots=True, ax=axes, sharex=True, sharey=True)
    for ax in axes:
        assert len(ax.lines) == 1
    for ax in [axes[0], axes[2]]:
        self._check_visible(ax.get_yticklabels(), visible=True)
    for ax in [axes[1], axes[3]]:
        self._check_visible(ax.get_yticklabels(), visible=False)
    for ax in [axes[0], axes[1]]:
        self._check_visible(ax.get_xticklabels(), visible=False)
        self._check_visible(ax.get_xticklabels(minor=True), visible=False)
    for ax in [axes[2], axes[3]]:
        self._check_visible(ax.get_xticklabels(), visible=True)
        self._check_visible(ax.get_xticklabels(minor=True), visible=True)
    tm.close()