def test_expanding_apply_args_kwargs(self, raw):

    def mean_w_arg(x, const):
        return np.mean(x) + const
    df = DataFrame(np.random.rand(20, 3))
    expected = df.expanding().apply(np.mean, raw=raw) + 20.0
    result = df.expanding().apply(mean_w_arg, raw=raw, args=(20,))
    tm.assert_frame_equal(result, expected)
    result = df.expanding().apply(mean_w_arg, raw=raw, kwargs={'const': 20})
    tm.assert_frame_equal(result, expected)