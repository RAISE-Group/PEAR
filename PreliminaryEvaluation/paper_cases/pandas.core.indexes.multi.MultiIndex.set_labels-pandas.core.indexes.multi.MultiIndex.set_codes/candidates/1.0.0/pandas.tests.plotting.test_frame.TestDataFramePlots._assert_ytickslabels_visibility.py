def _assert_ytickslabels_visibility(self, axes, expected):
    for ax, exp in zip(axes, expected):
        self._check_visible(ax.get_yticklabels(), visible=exp)