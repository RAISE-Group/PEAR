def test_categorical_dtype(self):
    assert com.pandas_dtype('category') == CategoricalDtype()