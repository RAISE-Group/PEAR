@pytest.mark.slow
def test_plot_offset_freq(self):
    ser = tm.makeTimeSeries()
    _check_plot_works(ser.plot)
    dr = date_range(ser.index[0], freq='BQS', periods=10)
    ser = Series(np.random.randn(len(dr)), index=dr)
    _check_plot_works(ser.plot)