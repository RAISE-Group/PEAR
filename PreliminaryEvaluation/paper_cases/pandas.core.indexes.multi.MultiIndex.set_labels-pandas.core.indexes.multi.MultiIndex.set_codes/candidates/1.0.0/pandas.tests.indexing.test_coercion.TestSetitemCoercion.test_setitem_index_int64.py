@pytest.mark.parametrize('val,exp_dtype', [(5, np.int64), (1.1, np.float64), ('x', np.object)])
def test_setitem_index_int64(self, val, exp_dtype):
    obj = pd.Series([1, 2, 3, 4])
    assert obj.index.dtype == np.int64
    exp_index = pd.Index([0, 1, 2, 3, val])
    self._assert_setitem_index_conversion(obj, val, exp_index, exp_dtype)