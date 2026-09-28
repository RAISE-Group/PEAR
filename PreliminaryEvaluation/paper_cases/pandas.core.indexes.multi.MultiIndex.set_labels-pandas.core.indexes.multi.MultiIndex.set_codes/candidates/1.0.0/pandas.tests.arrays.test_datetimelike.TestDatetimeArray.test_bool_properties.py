@pytest.mark.parametrize('propname', pd.DatetimeIndex._bool_ops)
def test_bool_properties(self, datetime_index, propname):
    dti = datetime_index
    arr = DatetimeArray(dti)
    assert dti.freq == arr.freq
    result = getattr(arr, propname)
    expected = np.array(getattr(dti, propname), dtype=result.dtype)
    tm.assert_numpy_array_equal(result, expected)