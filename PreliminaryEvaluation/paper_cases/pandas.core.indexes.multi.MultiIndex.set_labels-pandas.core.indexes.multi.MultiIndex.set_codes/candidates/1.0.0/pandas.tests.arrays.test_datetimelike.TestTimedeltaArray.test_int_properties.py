@pytest.mark.parametrize('propname', pd.TimedeltaIndex._field_ops)
def test_int_properties(self, timedelta_index, propname):
    tdi = timedelta_index
    arr = TimedeltaArray(tdi)
    result = getattr(arr, propname)
    expected = np.array(getattr(tdi, propname), dtype=result.dtype)
    tm.assert_numpy_array_equal(result, expected)