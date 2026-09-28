def test_api_compat(self):
    obj = self._construct(5)
    for func in ['sum', 'cumsum', 'any', 'var']:
        f = getattr(obj, func)
        assert f.__name__ == func
        assert f.__qualname__.endswith(func)