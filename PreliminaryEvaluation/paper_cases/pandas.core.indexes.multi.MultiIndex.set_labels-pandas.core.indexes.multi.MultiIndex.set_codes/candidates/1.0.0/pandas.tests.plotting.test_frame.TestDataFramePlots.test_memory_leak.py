@td.skip_if_no_scipy
def test_memory_leak(self):
    """ Check that every plot type gets properly collected. """
    import weakref
    import gc
    results = {}
    for kind in plotting.PlotAccessor._all_kinds:
        args = {}
        if kind in ['hexbin', 'scatter', 'pie']:
            df = self.hexbin_df
            args = {'x': 'A', 'y': 'B'}
        elif kind == 'area':
            df = self.tdf.abs()
        else:
            df = self.tdf
        results[kind] = weakref.proxy(df.plot(kind=kind, **args))
    tm.close()
    gc.collect()
    for key in results:
        with pytest.raises(ReferenceError):
            results[key].lines