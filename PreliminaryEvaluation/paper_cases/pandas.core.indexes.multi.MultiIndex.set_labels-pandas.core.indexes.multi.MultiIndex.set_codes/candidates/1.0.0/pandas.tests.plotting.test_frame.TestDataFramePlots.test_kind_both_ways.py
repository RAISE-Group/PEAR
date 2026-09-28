@td.skip_if_no_scipy
def test_kind_both_ways(self):
    df = DataFrame({'x': [1, 2, 3]})
    for kind in plotting.PlotAccessor._common_kinds:
        df.plot(kind=kind)
        getattr(df.plot, kind)()
    for kind in ['scatter', 'hexbin']:
        df.plot('x', 'x', kind=kind)
        getattr(df.plot, kind)('x', 'x')