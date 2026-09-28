def test_get_numeric_data(self):
    n = 4
    kwargs = {self._typ._AXIS_NAMES[i]: list(range(n)) for i in range(self._ndim)}
    o = self._construct(n, **kwargs)
    result = o._get_numeric_data()
    self._compare(result, o)
    result = o._get_bool_data()
    expected = self._construct(n, value='empty', **kwargs)
    self._compare(result, expected)
    arr = np.array([True, True, False, True])
    o = self._construct(n, value=arr, **kwargs)
    result = o._get_numeric_data()
    self._compare(result, o)