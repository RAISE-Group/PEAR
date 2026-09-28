@pytest.mark.parametrize('op', [operator.add, ops.radd])
def test_td_add_pytimedelta(self, op):
    td = Timedelta(10, unit='d')
    result = op(td, timedelta(days=9))
    assert isinstance(result, Timedelta)
    assert result == Timedelta(days=19)