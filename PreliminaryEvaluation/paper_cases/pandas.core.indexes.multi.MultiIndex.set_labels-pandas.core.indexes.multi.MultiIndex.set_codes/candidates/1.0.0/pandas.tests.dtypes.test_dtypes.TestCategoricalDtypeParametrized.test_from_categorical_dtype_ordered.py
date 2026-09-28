def test_from_categorical_dtype_ordered(self):
    c1 = Categorical([1, 2], categories=[1, 2, 3], ordered=True)
    result = CategoricalDtype._from_categorical_dtype(c1, ordered=False)
    assert result == CategoricalDtype([1, 2, 3], ordered=False)