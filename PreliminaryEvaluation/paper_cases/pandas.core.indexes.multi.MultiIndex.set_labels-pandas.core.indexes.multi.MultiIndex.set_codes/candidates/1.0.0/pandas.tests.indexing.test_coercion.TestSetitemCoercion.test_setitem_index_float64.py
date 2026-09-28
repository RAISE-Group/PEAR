@pytest.mark.parametrize('val,exp_dtype', [(5, IndexError), (5.1, np.float64), ('x', np.object)])
def test_setitem_index_float64(self, val, exp_dtype):
    obj = pd.Series([1, 2, 3, 4], index=[1.1, 2.1, 3.1, 4.1])
    assert obj.index.dtype == np.float64
    if exp_dtype is IndexError:
        temp = obj.copy()
        with pytest.raises(exp_dtype):
            temp[5] = 5
        pytest.xfail('TODO_GH12747 The result must be float')
    exp_index = pd.Index([1.1, 2.1, 3.1, 4.1, val])
    self._assert_setitem_index_conversion(obj, val, exp_index, exp_dtype)