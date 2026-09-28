def test_constructor_compound_dtypes(self):

    def f(dtype):
        data = list(itertools.repeat((datetime(2001, 1, 1), 'aa', 20), 9))
        return DataFrame(data=data, columns=['A', 'B', 'C'], dtype=dtype)
    msg = 'compound dtypes are not implemented in the DataFrame constructor'
    with pytest.raises(NotImplementedError, match=msg):
        f([('A', 'datetime64[h]'), ('B', 'str'), ('C', 'int32')])
    f('int64')
    f('float64')
    if not compat.is_platform_windows():
        f('M8[ns]')