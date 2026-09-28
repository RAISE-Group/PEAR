@pytest.mark.parametrize('op,nanop', [(operator.eq, nanops.naneq), (operator.ne, nanops.nanne), (operator.gt, nanops.nangt), (operator.ge, nanops.nange), (operator.lt, nanops.nanlt), (operator.le, nanops.nanle)])
def test_nan_comparison(self, op, nanop):
    targ0 = op(self.arr_float, self.arr_float1)
    self.check_nancomp(nanop, targ0)