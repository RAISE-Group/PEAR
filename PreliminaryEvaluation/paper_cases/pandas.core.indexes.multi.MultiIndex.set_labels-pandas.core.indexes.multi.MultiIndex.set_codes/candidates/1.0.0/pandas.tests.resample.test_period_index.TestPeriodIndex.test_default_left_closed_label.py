def test_default_left_closed_label(self):
    others = ['MS', 'AS', 'QS', 'D', 'H']
    others_freq = ['D', 'Q', 'M', 'H', 'T']
    for from_freq, to_freq in zip(others_freq, others):
        idx = date_range(start='8/15/2012', periods=100, freq=from_freq)
        df = DataFrame(np.random.randn(len(idx), 2), idx)
        resampled = df.resample(to_freq).mean()
        tm.assert_frame_equal(resampled, df.resample(to_freq, closed='left', label='left').mean())