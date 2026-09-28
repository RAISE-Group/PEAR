@pytest.mark.parametrize('q', [0.0, 0.1, 0.5, 0.9, 1.0])
def test_rolling_quantile(self, q, raw):

    def scoreatpercentile(a, per):
        values = np.sort(a, axis=0)
        idx = int(per / 1.0 * (values.shape[0] - 1))
        if idx == values.shape[0] - 1:
            retval = values[-1]
        else:
            qlow = float(idx) / float(values.shape[0] - 1)
            qhig = float(idx + 1) / float(values.shape[0] - 1)
            vlow = values[idx]
            vhig = values[idx + 1]
            retval = vlow + (vhig - vlow) * (per - qlow) / (qhig - qlow)
        return retval

    def quantile_func(x):
        return scoreatpercentile(x, q)
    self._check_moment_func(quantile_func, name='quantile', quantile=q, raw=raw)