def test_default_right_closed_label(self):
    end_freq = ['D', 'Q', 'M', 'D']
    end_types = ['M', 'A', 'Q', 'W']
    for from_freq, to_freq in zip(end_freq, end_types):
        idx = date_range(start='8/15/2012', periods=100, freq=from_freq)
        df = DataFrame(np.random.randn(len(idx), 2), idx)
        resampled = df.resample(to_freq).mean()
        tm.assert_frame_equal(resampled, df.resample(to_freq, closed='right', label='right').mean())