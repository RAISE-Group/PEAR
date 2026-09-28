@pytest.mark.slow
@pytest.mark.parametrize('cmp1', ['!=', '==', '<=', '>=', '<', '>'], ids=['ne', 'eq', 'le', 'ge', 'lt', 'gt'])
@pytest.mark.parametrize('cmp2', ['>', '<'], ids=['gt', 'lt'])
def test_complex_cmp_ops(self, cmp1, cmp2):
    for lhs, rhs, binop in product(self.lhses, self.rhses, self.bin_ops):
        lhs_new = _eval_single_bin(lhs, cmp1, rhs, self.engine)
        rhs_new = _eval_single_bin(lhs, cmp2, rhs, self.engine)
        expected = _eval_single_bin(lhs_new, binop, rhs_new, self.engine)
        ex = f'(lhs {cmp1} rhs) {binop} (lhs {cmp2} rhs)'
        result = pd.eval(ex, engine=self.engine, parser=self.parser)
        self.check_equal(result, expected)