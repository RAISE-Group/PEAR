def test_all_invalid_plot_data(self):
    df = DataFrame(list('abcd'))
    for kind in plotting.PlotAccessor._common_kinds:
        msg = 'no numeric data to plot'
        with pytest.raises(TypeError, match=msg):
            df.plot(kind=kind)