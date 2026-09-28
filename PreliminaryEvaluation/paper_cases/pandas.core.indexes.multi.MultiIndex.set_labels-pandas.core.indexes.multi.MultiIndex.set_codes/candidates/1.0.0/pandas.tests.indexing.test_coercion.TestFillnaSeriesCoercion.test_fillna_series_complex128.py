@pytest.mark.parametrize('fill_val,fill_dtype', [(1, np.complex128), (1.1, np.complex128), (1 + 1j, np.complex128), (True, np.object)])
def test_fillna_series_complex128(self, fill_val, fill_dtype):
    obj = pd.Series([1 + 1j, np.nan, 3 + 3j, 4 + 4j])
    assert obj.dtype == np.complex128
    exp = pd.Series([1 + 1j, fill_val, 3 + 3j, 4 + 4j])
    self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)