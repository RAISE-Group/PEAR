@pytest.mark.parametrize('propname', pd.DatetimeIndex._field_ops)
def test_int_properties(self, datetime_index, propname):
    dti = datetime_index
    arr = DatetimeArray(dti)
    result = getattr(arr, propname)
    expected = np.array(getattr(dti, propname), dtype=result.dtype)
    tm.assert_numpy_array_equal(result, expected)