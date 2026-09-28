def test_from_codes_with_nan_code(self):
    codes = [1, 2, np.nan]
    dtype = CategoricalDtype(categories=['a', 'b', 'c'])
    with pytest.raises(ValueError, match='codes need to be array-like integers'):
        Categorical.from_codes(codes, categories=dtype.categories)
    with pytest.raises(ValueError, match='codes need to be array-like integers'):
        Categorical.from_codes(codes, dtype=dtype)