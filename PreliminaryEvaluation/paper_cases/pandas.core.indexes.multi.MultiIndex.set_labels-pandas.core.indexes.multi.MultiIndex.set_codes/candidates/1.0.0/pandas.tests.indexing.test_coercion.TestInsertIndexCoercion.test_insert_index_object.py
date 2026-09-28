@pytest.mark.parametrize('insert, coerced_val, coerced_dtype', [(1, 1, np.object), (1.1, 1.1, np.object), (False, False, np.object), ('x', 'x', np.object)])
def test_insert_index_object(self, insert, coerced_val, coerced_dtype):
    obj = pd.Index(list('abcd'))
    assert obj.dtype == np.object
    exp = pd.Index(['a', coerced_val, 'b', 'c', 'd'])
    self._assert_insert_conversion(obj, insert, exp, coerced_dtype)