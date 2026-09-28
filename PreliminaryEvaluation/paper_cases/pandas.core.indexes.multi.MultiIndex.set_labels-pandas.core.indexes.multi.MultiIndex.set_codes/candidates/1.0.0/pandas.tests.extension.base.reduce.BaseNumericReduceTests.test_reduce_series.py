@pytest.mark.parametrize('skipna', [True, False])
def test_reduce_series(self, data, all_numeric_reductions, skipna):
    op_name = all_numeric_reductions
    s = pd.Series(data)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', RuntimeWarning)
        self.check_reduce(s, op_name, skipna)