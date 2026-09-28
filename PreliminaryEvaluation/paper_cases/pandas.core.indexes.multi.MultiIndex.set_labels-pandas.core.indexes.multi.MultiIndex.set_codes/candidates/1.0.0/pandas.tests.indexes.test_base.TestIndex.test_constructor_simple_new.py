@pytest.mark.parametrize('vals,dtype', [([1, 2, 3, 4, 5], 'int'), ([1.1, np.nan, 2.2, 3.0], 'float'), (['A', 'B', 'C', np.nan], 'obj')])
def test_constructor_simple_new(self, vals, dtype):
    index = Index(vals, name=dtype)
    result = index._simple_new(index.values, dtype)
    tm.assert_index_equal(result, index)