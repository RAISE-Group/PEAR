def test_from_codes(self):
    dtype = CategoricalDtype(categories=[1, 2])
    msg = 'codes need to be between '
    with pytest.raises(ValueError, match=msg):
        Categorical.from_codes([1, 2], categories=dtype.categories)
    with pytest.raises(ValueError, match=msg):
        Categorical.from_codes([1, 2], dtype=dtype)
    msg = 'codes need to be array-like integers'
    with pytest.raises(ValueError, match=msg):
        Categorical.from_codes(['a'], categories=dtype.categories)
    with pytest.raises(ValueError, match=msg):
        Categorical.from_codes(['a'], dtype=dtype)
    with pytest.raises(ValueError, match='Categorical categories must be unique'):
        Categorical.from_codes([0, 1, 2], categories=['a', 'a', 'b'])
    with pytest.raises(ValueError, match='Categorial categories cannot be null'):
        Categorical.from_codes([0, 1, 2], categories=['a', 'b', np.nan])
    dtype = CategoricalDtype(categories=['a', 'b', 'c'])
    msg = 'codes need to be between -1 and len\\(categories\\)-1'
    with pytest.raises(ValueError, match=msg):
        Categorical.from_codes([-2, 1, 2], categories=dtype.categories)
    with pytest.raises(ValueError, match=msg):
        Categorical.from_codes([-2, 1, 2], dtype=dtype)
    exp = Categorical(['a', 'b', 'c'], ordered=False)
    res = Categorical.from_codes([0, 1, 2], categories=dtype.categories)
    tm.assert_categorical_equal(exp, res)
    res = Categorical.from_codes([0, 1, 2], dtype=dtype)
    tm.assert_categorical_equal(exp, res)