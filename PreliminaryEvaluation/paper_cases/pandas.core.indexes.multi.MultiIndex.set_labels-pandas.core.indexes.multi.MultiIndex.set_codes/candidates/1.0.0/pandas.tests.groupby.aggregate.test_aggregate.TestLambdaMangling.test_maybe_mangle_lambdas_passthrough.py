def test_maybe_mangle_lambdas_passthrough(self):
    assert _maybe_mangle_lambdas('mean') == 'mean'
    assert _maybe_mangle_lambdas(lambda x: x).__name__ == '<lambda>'
    assert _maybe_mangle_lambdas([lambda x: x])[0].__name__ == '<lambda>'