@pytest.mark.parametrize('op', [operator.eq, operator.ne, operator.gt, operator.lt, operator.ge, operator.le])
def test_comparators(self, op):
    index = tm.makeDateIndex(100)
    element = index[len(index) // 2]
    element = Timestamp(element).to_datetime64()
    arr = np.array(index)
    arr_result = op(arr, element)
    index_result = op(index, element)
    assert isinstance(index_result, np.ndarray)
    tm.assert_numpy_array_equal(arr_result, index_result)