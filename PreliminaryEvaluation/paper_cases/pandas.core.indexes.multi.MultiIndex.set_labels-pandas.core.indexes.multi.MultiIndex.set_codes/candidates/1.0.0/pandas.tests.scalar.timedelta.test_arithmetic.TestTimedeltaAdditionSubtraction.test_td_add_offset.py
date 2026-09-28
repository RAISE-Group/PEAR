@pytest.mark.parametrize('op', [operator.add, ops.radd])
def test_td_add_offset(self, op):
    td = Timedelta(10, unit='d')
    result = op(td, offsets.Hour(6))
    assert isinstance(result, Timedelta)
    assert result == Timedelta(days=10, hours=6)