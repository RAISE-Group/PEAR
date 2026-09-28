def test_scatterplot_datetime_data(self):
    dates = pd.date_range(start=date(2019, 1, 1), periods=12, freq='W')
    vals = np.random.normal(0, 1, len(dates))
    df = pd.DataFrame({'dates': dates, 'vals': vals})
    _check_plot_works(df.plot.scatter, x='dates', y='vals')
    _check_plot_works(df.plot.scatter, x=0, y=1)