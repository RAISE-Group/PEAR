@pytest.mark.parametrize('propname', PeriodArray._field_ops)
def test_int_properties(self, period_index, propname):
    pi = period_index
    arr = PeriodArray(pi)
    result = getattr(arr, propname)
    expected = np.array(getattr(pi, propname))
    tm.assert_numpy_array_equal(result, expected)