@pytest.mark.slow
def test_line_plot_inferred_freq(self):
    for ser in self.datetime_ser:
        ser = Series(ser.values, Index(np.asarray(ser.index)))
        _check_plot_works(ser.plot, ser.index.inferred_freq)
        ser = ser[[0, 3, 5, 6]]
        _check_plot_works(ser.plot)