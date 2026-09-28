@pytest.mark.parametrize('insert, coerced_val, coerced_dtype', [(1, 1.0, np.float64), (1.1, 1.1, np.float64), (False, 0.0, np.float64), ('x', 'x', np.object)])
def test_insert_index_float64(self, insert, coerced_val, coerced_dtype):
    obj = pd.Float64Index([1.0, 2.0, 3.0, 4.0])
    assert obj.dtype == np.float64
    exp = pd.Index([1.0, coerced_val, 2.0, 3.0, 4.0])
    self._assert_insert_conversion(obj, insert, exp, coerced_dtype)