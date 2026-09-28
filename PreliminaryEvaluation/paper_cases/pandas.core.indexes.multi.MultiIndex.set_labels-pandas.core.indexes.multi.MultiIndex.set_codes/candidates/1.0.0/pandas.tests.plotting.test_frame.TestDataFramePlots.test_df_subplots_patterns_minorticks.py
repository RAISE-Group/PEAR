@pytest.mark.slow
def test_df_subplots_patterns_minorticks(self):
    import matplotlib.pyplot as plt
    df = DataFrame(np.random.randn(10, 2), index=date_range('1/1/2000', periods=10), columns=list('AB'))
    fig, axes = plt.subplots(2, 1, sharex=True)
    axes = df.plot(subplots=True, ax=axes)
    for ax in axes:
        assert len(ax.lines) == 1
        self._check_visible(ax.get_yticklabels(), visible=True)
    self._check_visible(axes[0].get_xticklabels(), visible=False)
    self._check_visible(axes[0].get_xticklabels(minor=True), visible=False)
    self._check_visible(axes[1].get_xticklabels(), visible=True)
    self._check_visible(axes[1].get_xticklabels(minor=True), visible=True)
    tm.close()
    fig, axes = plt.subplots(2, 1)
    with tm.assert_produces_warning(UserWarning):
        axes = df.plot(subplots=True, ax=axes, sharex=True)
    for ax in axes:
        assert len(ax.lines) == 1
        self._check_visible(ax.get_yticklabels(), visible=True)
    self._check_visible(axes[0].get_xticklabels(), visible=False)
    self._check_visible(axes[0].get_xticklabels(minor=True), visible=False)
    self._check_visible(axes[1].get_xticklabels(), visible=True)
    self._check_visible(axes[1].get_xticklabels(minor=True), visible=True)
    tm.close()
    fig, axes = plt.subplots(2, 1)
    axes = df.plot(subplots=True, ax=axes)
    for ax in axes:
        assert len(ax.lines) == 1
        self._check_visible(ax.get_yticklabels(), visible=True)
        self._check_visible(ax.get_xticklabels(), visible=True)
        self._check_visible(ax.get_xticklabels(minor=True), visible=True)
    tm.close()