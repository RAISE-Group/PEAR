@pytest.mark.slow
def test_plot_multiple_inferred_freq(self):
    dr = Index([datetime(2000, 1, 1), datetime(2000, 1, 6), datetime(2000, 1, 11)])
    ser = Series(np.random.randn(len(dr)), index=dr)
    _check_plot_works(ser.plot)