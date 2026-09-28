@pytest.mark.parametrize('values, categories, ordered, dtype, expected', [[None, None, None, None, CategoricalDtype()], [None, ['a', 'b'], True, None, dtype1], [c, None, None, dtype2, dtype2], [c, ['x', 'y'], False, None, dtype2]])
def test_from_values_or_dtype(self, values, categories, ordered, dtype, expected):
    result = CategoricalDtype._from_values_or_dtype(values, categories, ordered, dtype)
    assert result == expected