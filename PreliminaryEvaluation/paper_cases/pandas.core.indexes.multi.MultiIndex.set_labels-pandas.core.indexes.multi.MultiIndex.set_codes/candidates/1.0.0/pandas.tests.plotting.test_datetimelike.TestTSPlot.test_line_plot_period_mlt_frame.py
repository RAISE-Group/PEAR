@pytest.mark.slow
@pytest.mark.parametrize('frqncy', ['1S', '3S', '5T', '7H', '4D', '8W', '11M', '3A'])
def test_line_plot_period_mlt_frame(self, frqncy):
    idx = period_range('12/31/1999', freq=frqncy, periods=100)
    df = DataFrame(np.random.randn(len(idx), 3), index=idx, columns=['A', 'B', 'C'])
    freq = df.index.asfreq(df.index.freq.rule_code).freq
    _check_plot_works(df.plot, freq)