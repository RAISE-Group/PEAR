def test_from_categorical_dtype_identity(self):
    c1 = Categorical([1, 2], categories=[1, 2, 3], ordered=True)
    c2 = CategoricalDtype._from_categorical_dtype(c1)
    assert c2 is c1