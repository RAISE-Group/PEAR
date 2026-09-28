def check_simple_cmp_op(self, lhs, cmp1, rhs):
    ex = f'lhs {cmp1} rhs'
    msg = "only list-like( or dict-like)? objects are allowed to be passed to (DataFrame\\.)?isin\\(\\), you passed a (\\[|')bool(\\]|')|argument of type 'bool' is not iterable"
    if cmp1 in ('in', 'not in') and (not is_list_like(rhs)):
        with pytest.raises(TypeError, match=msg):
            pd.eval(ex, engine=self.engine, parser=self.parser, local_dict={'lhs': lhs, 'rhs': rhs})
    else:
        expected = _eval_single_bin(lhs, cmp1, rhs, self.engine)
        result = pd.eval(ex, engine=self.engine, parser=self.parser)
        self.check_equal(result, expected)