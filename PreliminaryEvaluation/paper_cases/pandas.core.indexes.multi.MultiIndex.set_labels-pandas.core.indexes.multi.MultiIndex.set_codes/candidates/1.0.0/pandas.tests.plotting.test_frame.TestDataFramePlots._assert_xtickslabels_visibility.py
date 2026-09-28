def _assert_xtickslabels_visibility(self, axes, expected):
    for ax, exp in zip(axes, expected):
        self._check_visible(ax.get_xticklabels(), visible=exp)