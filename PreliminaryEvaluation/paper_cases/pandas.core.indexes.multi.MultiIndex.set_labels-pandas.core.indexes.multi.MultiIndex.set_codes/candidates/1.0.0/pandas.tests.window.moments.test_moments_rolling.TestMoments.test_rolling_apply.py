def test_rolling_apply(self, raw):

    def f(x):
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', message='.*(empty slice|0 for slice).*', category=RuntimeWarning)
            return x[np.isfinite(x)].mean()
    self._check_moment_func(np.mean, name='apply', func=f, raw=raw)