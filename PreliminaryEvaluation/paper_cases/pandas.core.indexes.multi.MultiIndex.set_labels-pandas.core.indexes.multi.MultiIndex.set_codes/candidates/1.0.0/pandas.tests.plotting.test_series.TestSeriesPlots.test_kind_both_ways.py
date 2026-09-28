@pytest.mark.slow
def test_kind_both_ways(self):
    s = Series(range(3))
    kinds = plotting.PlotAccessor._common_kinds + plotting.PlotAccessor._series_kinds
    _, ax = self.plt.subplots()
    for kind in kinds:
        s.plot(kind=kind, ax=ax)
        getattr(s.plot, kind)()