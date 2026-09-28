@pytest.mark.parametrize('op', [operator.add, ops.radd])
@pytest.mark.parametrize('other', ['category', 'Int64'])
def test_add_extension_scalar(self, other, box_with_array, op):
    arr = pd.Series(['a', 'b', 'c'])
    expected = pd.Series([op(x, other) for x in arr])
    arr = tm.box_expected(arr, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    result = op(arr, other)
    tm.assert_equal(result, expected)