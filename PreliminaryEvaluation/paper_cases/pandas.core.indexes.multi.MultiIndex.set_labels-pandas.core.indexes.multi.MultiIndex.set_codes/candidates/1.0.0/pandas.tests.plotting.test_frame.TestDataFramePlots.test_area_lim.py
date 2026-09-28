def test_area_lim(self):
    df = DataFrame(rand(6, 4), columns=['x', 'y', 'z', 'four'])
    neg_df = -df
    for stacked in [True, False]:
        ax = _check_plot_works(df.plot.area, stacked=stacked)
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        lines = ax.get_lines()
        assert xmin <= lines[0].get_data()[0][0]
        assert xmax >= lines[0].get_data()[0][-1]
        assert ymin == 0
        ax = _check_plot_works(neg_df.plot.area, stacked=stacked)
        ymin, ymax = ax.get_ylim()
        assert ymax == 0