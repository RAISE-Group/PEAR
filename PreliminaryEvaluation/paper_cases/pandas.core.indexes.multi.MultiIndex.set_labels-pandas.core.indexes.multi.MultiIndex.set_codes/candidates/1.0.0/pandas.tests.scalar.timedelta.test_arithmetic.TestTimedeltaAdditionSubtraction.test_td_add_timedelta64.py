@pytest.mark.parametrize('op', [operator.add, ops.radd])
def test_td_add_timedelta64(self, op):
    td = Timedelta(10, unit='d')
    result = op(td, np.timedelta64(-4, 'D'))
    assert isinstance(result, Timedelta)
    assert result == Timedelta(days=6)