@pytest.mark.slow
def test_high_freq(self):
    freaks = ['ms', 'us']
    for freq in freaks:
        _, ax = self.plt.subplots()
        rng = date_range('1/1/2012', periods=100, freq=freq)
        ser = Series(np.random.randn(len(rng)), rng)
        _check_plot_works(ser.plot, ax=ax)