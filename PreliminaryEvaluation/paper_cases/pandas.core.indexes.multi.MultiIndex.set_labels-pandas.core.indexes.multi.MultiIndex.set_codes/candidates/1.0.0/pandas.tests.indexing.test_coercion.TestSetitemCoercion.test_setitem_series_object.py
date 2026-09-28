@pytest.mark.parametrize('val,exp_dtype', [(1, np.object), (1.1, np.object), (1 + 1j, np.object), (True, np.object)])
def test_setitem_series_object(self, val, exp_dtype):
    obj = pd.Series(list('abcd'))
    assert obj.dtype == np.object
    exp = pd.Series(['a', val, 'c', 'd'])
    self._assert_setitem_series_conversion(obj, val, exp, exp_dtype)