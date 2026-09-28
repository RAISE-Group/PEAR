def test_rgb_tuple_color(self):
    df = DataFrame({'x': [1, 2], 'y': [3, 4]})
    _check_plot_works(df.plot, x='x', y='y', color=(1, 0, 0))
    _check_plot_works(df.plot, x='x', y='y', color=(1, 0, 0, 0.5))