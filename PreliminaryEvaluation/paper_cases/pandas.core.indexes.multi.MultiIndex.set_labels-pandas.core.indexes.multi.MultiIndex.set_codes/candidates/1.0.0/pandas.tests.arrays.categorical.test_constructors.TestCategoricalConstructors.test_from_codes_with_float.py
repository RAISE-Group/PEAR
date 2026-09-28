def test_from_codes_with_float(self):
    codes = [1.0, 2.0, 0]
    dtype = CategoricalDtype(categories=['a', 'b', 'c'])
    Categorical.from_codes([], dtype.categories)
    with pytest.raises(ValueError, match='codes need to be array-like integers'):
        Categorical.from_codes(codes, dtype.categories)
    with pytest.raises(ValueError, match='codes need to be array-like integers'):
        Categorical.from_codes(codes, dtype=dtype)
    codes = [1.1, 2.0, 0]
    with pytest.raises(ValueError, match='codes need to be array-like integers'):
        Categorical.from_codes(codes, dtype.categories)
    with pytest.raises(ValueError, match='codes need to be array-like integers'):
        Categorical.from_codes(codes, dtype=dtype)