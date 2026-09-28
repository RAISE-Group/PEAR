@pytest.mark.parametrize('op_str,opname', [('+', 'add'), ('*', 'mul'), ('-', 'sub')])
def test_bool_ops_warn_on_arithmetic(self, op_str, opname):
    n = 10
    df = DataFrame({'a': np.random.rand(n) > 0.5, 'b': np.random.rand(n) > 0.5})
    subs = {'+': '|', '*': '&', '-': '^'}
    sub_funcs = {'|': 'or_', '&': 'and_', '^': 'xor'}
    f = getattr(operator, opname)
    fe = getattr(operator, sub_funcs[subs[op_str]])
    if op_str == '-':
        return
    with tm.use_numexpr(True, min_elements=5):
        with tm.assert_produces_warning(check_stacklevel=False):
            r = f(df, df)
            e = fe(df, df)
            tm.assert_frame_equal(r, e)
        with tm.assert_produces_warning(check_stacklevel=False):
            r = f(df.a, df.b)
            e = fe(df.a, df.b)
            tm.assert_series_equal(r, e)
        with tm.assert_produces_warning(check_stacklevel=False):
            r = f(df.a, True)
            e = fe(df.a, True)
            tm.assert_series_equal(r, e)
        with tm.assert_produces_warning(check_stacklevel=False):
            r = f(False, df.a)
            e = fe(False, df.a)
            tm.assert_series_equal(r, e)
        with tm.assert_produces_warning(check_stacklevel=False):
            r = f(False, df)
            e = fe(False, df)
            tm.assert_frame_equal(r, e)
        with tm.assert_produces_warning(check_stacklevel=False):
            r = f(df, True)
            e = fe(df, True)
            tm.assert_frame_equal(r, e)