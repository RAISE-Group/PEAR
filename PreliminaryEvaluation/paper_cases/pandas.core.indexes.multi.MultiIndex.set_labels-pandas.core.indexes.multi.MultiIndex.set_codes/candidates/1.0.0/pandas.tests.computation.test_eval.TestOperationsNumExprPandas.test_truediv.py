def test_truediv(self):
    s = np.array([1])
    ex = 's / 1'
    d = {'s': s}
    with tm.assert_produces_warning(FutureWarning):
        res = self.eval(ex, truediv=False)
    tm.assert_numpy_array_equal(res, np.array([1.0]))
    with tm.assert_produces_warning(FutureWarning):
        res = self.eval(ex, truediv=True)
    tm.assert_numpy_array_equal(res, np.array([1.0]))
    with tm.assert_produces_warning(FutureWarning):
        res = self.eval('1 / 2', truediv=True)
    expec = 0.5
    assert res == expec
    with tm.assert_produces_warning(FutureWarning):
        res = self.eval('1 / 2', truediv=False)
    expec = 0.5
    assert res == expec
    with tm.assert_produces_warning(FutureWarning):
        res = self.eval('s / 2', truediv=False)
    expec = 0.5
    assert res == expec
    with tm.assert_produces_warning(FutureWarning):
        res = self.eval('s / 2', truediv=True)
    expec = 0.5
    assert res == expec