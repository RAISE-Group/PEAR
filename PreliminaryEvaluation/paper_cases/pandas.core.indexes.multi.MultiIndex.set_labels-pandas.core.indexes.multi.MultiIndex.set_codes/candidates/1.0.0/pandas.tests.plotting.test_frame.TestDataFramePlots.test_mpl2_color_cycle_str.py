def test_mpl2_color_cycle_str(self):
    colors = ['C' + str(x) for x in range(10)]
    df = DataFrame(randn(10, 3), columns=['a', 'b', 'c'])
    for c in colors:
        _check_plot_works(df.plot, color=c)