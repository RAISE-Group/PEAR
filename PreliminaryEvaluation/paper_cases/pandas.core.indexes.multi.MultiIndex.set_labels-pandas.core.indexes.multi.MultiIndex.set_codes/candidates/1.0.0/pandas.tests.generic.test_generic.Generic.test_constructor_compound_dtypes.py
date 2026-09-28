def test_constructor_compound_dtypes(self):

    def f(dtype):
        return self._construct(shape=3, value=1, dtype=dtype)
    msg = 'compound dtypes are not implemented'
    f'in the {self._typ.__name__} constructor'
    with pytest.raises(NotImplementedError, match=msg):
        f([('A', 'datetime64[h]'), ('B', 'str'), ('C', 'int32')])
    f('int64')
    f('float64')
    f('M8[ns]')