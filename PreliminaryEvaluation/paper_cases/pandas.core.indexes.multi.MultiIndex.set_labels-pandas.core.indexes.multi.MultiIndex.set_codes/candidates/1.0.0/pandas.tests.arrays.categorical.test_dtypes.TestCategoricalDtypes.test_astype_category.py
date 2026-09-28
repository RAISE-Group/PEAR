@pytest.mark.parametrize('dtype_ordered', [True, False])
@pytest.mark.parametrize('cat_ordered', [True, False])
def test_astype_category(self, dtype_ordered, cat_ordered):
    data = list('abcaacbab')
    cat = Categorical(data, categories=list('bac'), ordered=cat_ordered)
    dtype = CategoricalDtype(ordered=dtype_ordered)
    result = cat.astype(dtype)
    expected = Categorical(data, categories=cat.categories, ordered=dtype_ordered)
    tm.assert_categorical_equal(result, expected)
    dtype = CategoricalDtype(list('adc'), dtype_ordered)
    result = cat.astype(dtype)
    expected = Categorical(data, dtype=dtype)
    tm.assert_categorical_equal(result, expected)
    if dtype_ordered is False:
        result = cat.astype('category')
        expected = cat
        tm.assert_categorical_equal(result, expected)