@pytest.mark.parametrize('nan_op,np_op', [(nanops.nanany, np.any), (nanops.nanall, np.all)])
def test_nan_funcs(self, nan_op, np_op):
    self.check_funs(nan_op, np_op, allow_all_nan=False, allow_date=False, allow_tdelta=False)