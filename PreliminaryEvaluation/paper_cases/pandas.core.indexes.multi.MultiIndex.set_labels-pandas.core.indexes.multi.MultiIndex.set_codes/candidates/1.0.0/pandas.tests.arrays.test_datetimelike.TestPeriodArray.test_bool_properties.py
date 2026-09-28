@pytest.mark.parametrize('propname', PeriodArray._bool_ops)
def test_bool_properties(self, period_index, propname):
    pi = period_index
    arr = PeriodArray(pi)
    result = getattr(arr, propname)
    expected = np.array(getattr(pi, propname))
    tm.assert_numpy_array_equal(result, expected)