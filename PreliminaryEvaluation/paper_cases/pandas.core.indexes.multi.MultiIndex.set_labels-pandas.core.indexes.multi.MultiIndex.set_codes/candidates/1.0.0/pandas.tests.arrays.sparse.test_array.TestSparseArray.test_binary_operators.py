@pytest.mark.parametrize('op', ['add', 'sub', 'mul', 'truediv', 'floordiv', 'pow'])
def test_binary_operators(self, op):
    op = getattr(operator, op)
    data1 = np.random.randn(20)
    data2 = np.random.randn(20)
    data1[::2] = np.nan
    data2[::3] = np.nan
    arr1 = SparseArray(data1)
    arr2 = SparseArray(data2)
    data1[::2] = 3
    data2[::3] = 3
    farr1 = SparseArray(data1, fill_value=3)
    farr2 = SparseArray(data2, fill_value=3)

    def _check_op(op, first, second):
        res = op(first, second)
        exp = SparseArray(op(first.to_dense(), second.to_dense()), fill_value=first.fill_value)
        assert isinstance(res, SparseArray)
        tm.assert_almost_equal(res.to_dense(), exp.to_dense())
        res2 = op(first, second.to_dense())
        assert isinstance(res2, SparseArray)
        tm.assert_sp_array_equal(res, res2)
        res3 = op(first.to_dense(), second)
        assert isinstance(res3, SparseArray)
        tm.assert_sp_array_equal(res, res3)
        res4 = op(first, 4)
        assert isinstance(res4, SparseArray)
        try:
            exp = op(first.to_dense(), 4)
            exp_fv = op(first.fill_value, 4)
        except ValueError:
            pass
        else:
            tm.assert_almost_equal(res4.fill_value, exp_fv)
            tm.assert_almost_equal(res4.to_dense(), exp)
    with np.errstate(all='ignore'):
        for first_arr, second_arr in [(arr1, arr2), (farr1, farr2)]:
            _check_op(op, first_arr, second_arr)