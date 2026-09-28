def test_scatterplot_object_data(self):
    df = pd.DataFrame(dict(a=['A', 'B', 'C'], b=[2, 3, 4]))
    _check_plot_works(df.plot.scatter, x='a', y='b')
    _check_plot_works(df.plot.scatter, x=0, y=1)
    df = pd.DataFrame(dict(a=['A', 'B', 'C'], b=['a', 'b', 'c']))
    _check_plot_works(df.plot.scatter, x='a', y='b')
    _check_plot_works(df.plot.scatter, x=0, y=1)