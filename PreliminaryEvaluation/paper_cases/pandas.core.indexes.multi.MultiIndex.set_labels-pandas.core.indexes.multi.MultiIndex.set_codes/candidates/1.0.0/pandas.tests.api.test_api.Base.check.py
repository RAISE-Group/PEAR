def check(self, namespace, expected, ignored=None):
    result = sorted((f for f in dir(namespace) if not f.startswith('__')))
    if ignored is not None:
        result = sorted(set(result) - set(ignored))
    expected = sorted(expected)
    tm.assert_almost_equal(result, expected)