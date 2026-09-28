@pytest.mark.slow
def test_valid_object_plot(self):
    s = Series(range(10), dtype=object)
    for kind in plotting.PlotAccessor._common_kinds:
        _check_plot_works(s.plot, kind=kind)