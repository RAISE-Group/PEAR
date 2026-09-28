@pytest.mark.parametrize('val,exp_dtype', [('x', np.object), (5, IndexError), (1.1, np.object)])
def test_setitem_index_object(self, val, exp_dtype):
    obj = pd.Series([1, 2, 3, 4], index=list('abcd'))
    assert obj.index.dtype == np.object
    if exp_dtype is IndexError:
        temp = obj.copy()
        with pytest.raises(exp_dtype):
            temp[5] = 5
    else:
        exp_index = pd.Index(list('abcd') + [val])
        self._assert_setitem_index_conversion(obj, val, exp_index, exp_dtype)