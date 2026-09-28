@pytest.mark.parametrize('jit', [True, False])
def test_cache(self, jit, nogil, parallel, nopython):

    def func_1(x):
        return np.mean(x) + 4

    def func_2(x):
        return np.std(x) * 5
    if jit:
        import numba
        func_1 = numba.jit(func_1)
        func_2 = numba.jit(func_2)
    engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
    roll = Series(range(10)).rolling(2)
    result = roll.apply(func_1, engine='numba', engine_kwargs=engine_kwargs, raw=True)
    expected = roll.apply(func_1, engine='cython', raw=True)
    tm.assert_series_equal(result, expected)
    assert func_1 in roll._numba_func_cache
    result = roll.apply(func_2, engine='numba', engine_kwargs=engine_kwargs, raw=True)
    expected = roll.apply(func_2, engine='cython', raw=True)
    tm.assert_series_equal(result, expected)
    result = roll.apply(func_1, engine='numba', engine_kwargs=engine_kwargs, raw=True)
    expected = roll.apply(func_1, engine='cython', raw=True)
    tm.assert_series_equal(result, expected)