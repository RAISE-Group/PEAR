@pytest.mark.parametrize('arg ,expected', [(('1', '1', '2'), np.array(['1', '2'], dtype=object)), (('foo',), np.array(['foo'], dtype=object))])
def test_tuple_with_strings(self, arg, expected):
    result = pd.unique(arg)
    tm.assert_numpy_array_equal(result, expected)