@pytest.mark.parametrize('nan_op,np_op', [(nanops.nanmin, np.min), (nanops.nanmax, np.max)])
def test_nanops_with_warnings(self, nan_op, np_op):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('ignore', RuntimeWarning)
        self.check_funs(nan_op, np_op, allow_obj=False)