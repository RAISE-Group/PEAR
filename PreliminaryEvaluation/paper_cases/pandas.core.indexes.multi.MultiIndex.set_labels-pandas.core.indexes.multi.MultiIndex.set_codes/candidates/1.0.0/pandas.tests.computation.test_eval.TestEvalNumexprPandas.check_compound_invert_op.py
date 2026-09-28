def check_compound_invert_op(self, lhs, cmp1, rhs):
    skip_these = ['in', 'not in']
    ex = f'~(lhs {cmp1} rhs)'
    msg = "only list-like( or dict-like)? objects are allowed to be passed to (DataFrame\\.)?isin\\(\\), you passed a (\\[|')float(\\]|')|argument of type 'float' is not iterable"
    if is_scalar(rhs) and cmp1 in skip_these:
        with pytest.raises(TypeError, match=msg):
            pd.eval(ex, engine=self.engine, parser=self.parser, local_dict={'lhs': lhs, 'rhs': rhs})
    else:
        if is_scalar(lhs) and is_scalar(rhs):
            lhs, rhs = map(lambda x: np.array([x]), (lhs, rhs))
        expected = _eval_single_bin(lhs, cmp1, rhs, self.engine)
        if is_scalar(expected):
            expected = not expected
        else:
            expected = ~expected
        result = pd.eval(ex, engine=self.engine, parser=self.parser)
        tm.assert_almost_equal(expected, result)
        for engine in self.current_engines:
            ev = pd.eval(ex, engine=self.engine, parser=self.parser)
            tm.assert_almost_equal(ev, result)