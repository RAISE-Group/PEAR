@pytest.mark.slow
def test_frame_inferred(self):
    idx = date_range('1/1/1987', freq='MS', periods=100)
    idx = DatetimeIndex(idx.values, freq=None)
    df = DataFrame(np.random.randn(len(idx), 3), index=idx)
    _check_plot_works(df.plot)
    idx = idx[0:40].union(idx[45:99])
    df2 = DataFrame(np.random.randn(len(idx), 3), index=idx)
    _check_plot_works(df2.plot)
    idx = date_range('2008-1-1 00:15:00', freq='15T', periods=10)
    idx = DatetimeIndex(idx.values, freq=None)
    df = DataFrame(np.random.randn(len(idx), 3), index=idx)
    _check_plot_works(df.plot)