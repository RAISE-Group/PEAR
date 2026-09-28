def test_maybe_mangle_lambdas_named(self):
    func = {'C': np.mean, 'D': {'foo': np.mean, 'bar': np.mean}}
    result = _maybe_mangle_lambdas(func)
    assert result == func