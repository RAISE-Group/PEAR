@pytest.mark.parametrize('op', [operator.mul, ops.rmul])
def test_td_mul_scalar(self, op):
    td = Timedelta(minutes=3)
    result = op(td, 2)
    assert result == Timedelta(minutes=6)
    result = op(td, 1.5)
    assert result == Timedelta(minutes=4, seconds=30)
    assert op(td, np.nan) is NaT
    assert op(-1, td).value == -1 * td.value
    assert op(-1.0, td).value == -1.0 * td.value
    with pytest.raises(TypeError):
        op(td, Timestamp(2016, 1, 2))
    with pytest.raises(TypeError):
        op(td, td)