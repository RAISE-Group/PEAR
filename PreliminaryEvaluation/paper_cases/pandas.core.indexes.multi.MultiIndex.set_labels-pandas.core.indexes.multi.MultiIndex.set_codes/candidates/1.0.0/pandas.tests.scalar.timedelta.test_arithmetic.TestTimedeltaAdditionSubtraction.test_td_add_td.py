@pytest.mark.parametrize('op', [operator.add, ops.radd])
def test_td_add_td(self, op):
    td = Timedelta(10, unit='d')
    result = op(td, Timedelta(days=10))
    assert isinstance(result, Timedelta)
    assert result == Timedelta(days=20)