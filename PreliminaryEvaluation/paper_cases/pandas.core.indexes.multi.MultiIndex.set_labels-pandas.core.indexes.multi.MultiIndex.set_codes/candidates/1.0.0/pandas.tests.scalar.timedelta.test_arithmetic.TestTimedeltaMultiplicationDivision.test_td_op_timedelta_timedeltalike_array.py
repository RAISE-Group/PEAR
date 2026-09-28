@pytest.mark.parametrize('op', [operator.mul, ops.rmul, operator.truediv, ops.rdiv, ops.rsub])
@pytest.mark.parametrize('arr', [np.array([Timestamp('20130101 9:01'), Timestamp('20121230 9:02')]), np.array([Timestamp.now(), Timedelta('1D')])])
def test_td_op_timedelta_timedeltalike_array(self, op, arr):
    with pytest.raises(TypeError):
        op(arr, Timedelta('1D'))