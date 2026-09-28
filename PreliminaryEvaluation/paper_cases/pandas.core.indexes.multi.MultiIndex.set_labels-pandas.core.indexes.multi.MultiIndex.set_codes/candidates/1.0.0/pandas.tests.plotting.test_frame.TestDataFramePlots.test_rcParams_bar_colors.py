def test_rcParams_bar_colors(self):
    import matplotlib as mpl
    color_tuples = [(0.9, 0, 0, 1), (0, 0.9, 0, 1), (0, 0, 0.9, 1)]
    with mpl.rc_context(rc={'axes.prop_cycle': mpl.cycler('color', color_tuples)}):
        barplot = pd.DataFrame([[1, 2, 3]]).plot(kind='bar')
    assert color_tuples == [c.get_facecolor() for c in barplot.patches]