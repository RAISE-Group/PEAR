@pytest.mark.parametrize('values, categories, ordered, dtype', [[None, ['a', 'b'], True, dtype2], [None, ['a', 'b'], None, dtype2], [None, None, True, dtype2]])
def test_from_values_or_dtype_raises(self, values, categories, ordered, dtype):
    msg = 'Cannot specify `categories` or `ordered` together with `dtype`.'
    with pytest.raises(ValueError, match=msg):
        CategoricalDtype._from_values_or_dtype(values, categories, ordered, dtype)