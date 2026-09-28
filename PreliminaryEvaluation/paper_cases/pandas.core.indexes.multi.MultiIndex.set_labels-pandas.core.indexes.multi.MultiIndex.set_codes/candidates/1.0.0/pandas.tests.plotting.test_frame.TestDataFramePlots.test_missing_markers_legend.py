def test_missing_markers_legend(self):
    df = pd.DataFrame(np.random.randn(8, 3), columns=['A', 'B', 'C'])
    ax = df.plot(y=['A'], marker='x', linestyle='solid')
    df.plot(y=['B'], marker='o', linestyle='dotted', ax=ax)
    df.plot(y=['C'], marker='<', linestyle='dotted', ax=ax)
    self._check_legend_labels(ax, labels=['A', 'B', 'C'])
    self._check_legend_marker(ax, expected_markers=['x', 'o', '<'])