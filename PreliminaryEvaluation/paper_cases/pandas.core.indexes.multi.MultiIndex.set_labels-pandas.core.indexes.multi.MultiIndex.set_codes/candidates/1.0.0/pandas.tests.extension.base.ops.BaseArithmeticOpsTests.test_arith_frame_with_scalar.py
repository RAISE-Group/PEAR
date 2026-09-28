@pytest.mark.xfail(run=False, reason='_reduce needs implementation')
def test_arith_frame_with_scalar(self, data, all_arithmetic_operators):
    op_name = all_arithmetic_operators
    df = pd.DataFrame({'A': data})
    self.check_opname(df, op_name, data[0], exc=self.frame_scalar_exc)