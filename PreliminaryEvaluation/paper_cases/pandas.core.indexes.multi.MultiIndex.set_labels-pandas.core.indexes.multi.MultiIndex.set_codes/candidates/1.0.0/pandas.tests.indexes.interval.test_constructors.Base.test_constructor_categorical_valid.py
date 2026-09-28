@pytest.mark.parametrize('cat_constructor', [Categorical, CategoricalIndex])
def test_constructor_categorical_valid(self, constructor, cat_constructor):
    if isinstance(constructor, partial) and constructor.func is Index:
        pytest.skip()
    breaks = np.arange(10, dtype='int64')
    expected = IntervalIndex.from_breaks(breaks)
    cat_breaks = cat_constructor(breaks)
    result_kwargs = self.get_kwargs_from_breaks(cat_breaks)
    result = constructor(**result_kwargs)
    tm.assert_index_equal(result, expected)