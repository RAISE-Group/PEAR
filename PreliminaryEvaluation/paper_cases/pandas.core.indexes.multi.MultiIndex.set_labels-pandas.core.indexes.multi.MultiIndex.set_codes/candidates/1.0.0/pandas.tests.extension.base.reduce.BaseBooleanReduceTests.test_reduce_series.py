@pytest.mark.parametrize('skipna', [True, False])
def test_reduce_series(self, data, all_boolean_reductions, skipna):
    op_name = all_boolean_reductions
    s = pd.Series(data)
    self.check_reduce(s, op_name, skipna)