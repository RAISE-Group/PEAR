@pytest.mark.slow
def test_no_legend(self):
    kinds = ['line', 'bar', 'barh', 'kde', 'area', 'hist']
    df = DataFrame(rand(3, 3), columns=['a', 'b', 'c'])
    for kind in kinds:
        ax = df.plot(kind=kind, legend=False)
        self._check_legend_labels(ax, visible=False)