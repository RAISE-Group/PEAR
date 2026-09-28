@pytest.mark.parametrize('op', [operator.add, ops.radd])
def test_td_add_mixed_timedeltalike_object_dtype_array(self, op):
    now = Timestamp.now()
    arr = np.array([now, Timedelta('1D')])
    exp = np.array([now + Timedelta('1D'), Timedelta('2D')])
    res = op(arr, Timedelta('1D'))
    tm.assert_numpy_array_equal(res, exp)