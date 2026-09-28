@pytest.mark.parametrize('copy', [True, False])
@pytest.mark.parametrize('name', [None, 'foo'])
@pytest.mark.parametrize('ordered', [True, False])
def test_astype_category(self, copy, name, ordered):
    index = self.create_index()
    if name:
        index = index.rename(name)
    dtype = CategoricalDtype(ordered=ordered)
    result = index.astype(dtype, copy=copy)
    expected = CategoricalIndex(index.values, name=name, ordered=ordered)
    tm.assert_index_equal(result, expected)
    dtype = CategoricalDtype(index.unique().tolist()[:-1], ordered)
    result = index.astype(dtype, copy=copy)
    expected = CategoricalIndex(index.values, name=name, dtype=dtype)
    tm.assert_index_equal(result, expected)
    if ordered is False:
        result = index.astype('category', copy=copy)
        expected = CategoricalIndex(index.values, name=name)
        tm.assert_index_equal(result, expected)