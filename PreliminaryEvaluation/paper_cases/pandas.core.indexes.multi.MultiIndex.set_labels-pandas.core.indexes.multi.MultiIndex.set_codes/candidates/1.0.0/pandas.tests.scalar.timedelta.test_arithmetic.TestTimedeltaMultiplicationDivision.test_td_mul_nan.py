@pytest.mark.parametrize('nan', [np.nan, np.float64('NaN'), float('nan')])
@pytest.mark.parametrize('op', [operator.mul, ops.rmul])
def test_td_mul_nan(self, op, nan):
    td = Timedelta(10, unit='d')
    result = op(td, nan)
    assert result is NaT