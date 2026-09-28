@pytest.mark.parametrize('name', [None, 'foo'])
@pytest.mark.parametrize('dtype_ordered', [True, False])
@pytest.mark.parametrize('index_ordered', [True, False])
def test_astype_category(self, name, dtype_ordered, index_ordered):
    index = self.create_index(ordered=index_ordered)
    if name:
        index = index.rename(name)
    dtype = CategoricalDtype(ordered=dtype_ordered)
    result = index.astype(dtype)
    expected = CategoricalIndex(index.tolist(), name=name, categories=index.categories, ordered=dtype_ordered)
    tm.assert_index_equal(result, expected)
    dtype = CategoricalDtype(index.unique().tolist()[:-1], dtype_ordered)
    result = index.astype(dtype)
    expected = CategoricalIndex(index.tolist(), name=name, dtype=dtype)
    tm.assert_index_equal(result, expected)
    if dtype_ordered is False:
        result = index.astype('category')
        expected = index
        tm.assert_index_equal(result, expected)