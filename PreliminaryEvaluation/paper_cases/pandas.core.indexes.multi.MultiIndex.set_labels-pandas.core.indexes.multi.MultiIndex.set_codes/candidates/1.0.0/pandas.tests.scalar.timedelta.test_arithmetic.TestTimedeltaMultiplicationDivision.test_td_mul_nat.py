@pytest.mark.parametrize('td_nat', [NaT, np.timedelta64('NaT', 'ns'), np.timedelta64('NaT')])
@pytest.mark.parametrize('op', [operator.mul, ops.rmul])
def test_td_mul_nat(self, op, td_nat):
    td = Timedelta(10, unit='d')
    with pytest.raises(TypeError):
        op(td, td_nat)