def test_color_single_series_list(self):
    df = DataFrame({'A': [1, 2, 3]})
    _check_plot_works(df.plot, color=['red'])