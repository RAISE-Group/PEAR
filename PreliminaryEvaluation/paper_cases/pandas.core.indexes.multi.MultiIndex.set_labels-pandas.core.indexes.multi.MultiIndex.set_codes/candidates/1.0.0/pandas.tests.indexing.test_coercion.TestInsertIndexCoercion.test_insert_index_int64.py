@pytest.mark.parametrize('insert, coerced_val, coerced_dtype', [(1, 1, np.int64), (1.1, 1.1, np.float64), (False, 0, np.int64), ('x', 'x', np.object)])
def test_insert_index_int64(self, insert, coerced_val, coerced_dtype):
    obj = pd.Int64Index([1, 2, 3, 4])
    assert obj.dtype == np.int64
    exp = pd.Index([1, coerced_val, 2, 3, 4])
    self._assert_insert_conversion(obj, insert, exp, coerced_dtype)