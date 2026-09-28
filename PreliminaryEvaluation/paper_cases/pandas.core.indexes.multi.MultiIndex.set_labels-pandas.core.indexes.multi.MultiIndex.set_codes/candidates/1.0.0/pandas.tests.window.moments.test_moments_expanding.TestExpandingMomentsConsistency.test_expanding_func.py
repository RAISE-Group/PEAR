@pytest.mark.parametrize('has_min_periods', [True, False])
@pytest.mark.parametrize('func,static_comp', [('sum', np.sum), ('mean', np.mean), ('max', np.max), ('min', np.min)], ids=['sum', 'mean', 'max', 'min'])
def test_expanding_func(self, func, static_comp, has_min_periods):

    def expanding_func(x, min_periods=1, center=False, axis=0):
        exp = x.expanding(min_periods=min_periods, center=center, axis=axis)
        return getattr(exp, func)()
    self._check_expanding(expanding_func, static_comp, preserve_nan=False)
    self._check_expanding_has_min_periods(expanding_func, static_comp, has_min_periods)