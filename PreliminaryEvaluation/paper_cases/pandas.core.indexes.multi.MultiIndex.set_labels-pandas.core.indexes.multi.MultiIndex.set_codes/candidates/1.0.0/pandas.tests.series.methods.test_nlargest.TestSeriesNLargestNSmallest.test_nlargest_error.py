@pytest.mark.parametrize('r', [Series([3.0, 2, 1, 2, '5'], dtype='object'), Series([3.0, 2, 1, 2, 5], dtype='object'), Series([3.0, 2, 1, 2, 5], dtype='complex128'), Series(list('abcde')), Series(list('abcde'), dtype='category')])
def test_nlargest_error(self, r):
    dt = r.dtype
    msg = "Cannot use method 'n(larg|small)est' with dtype {dt}".format(dt=dt)
    args = (2, len(r), 0, -1)
    methods = (r.nlargest, r.nsmallest)
    for method, arg in product(methods, args):
        with pytest.raises(TypeError, match=msg):
            method(arg)