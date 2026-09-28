def test_constructor_dtype_and_others_raises(self):
    dtype = CategoricalDtype(['a', 'b'], ordered=True)
    msg = 'Cannot specify `categories` or `ordered` together with `dtype`.'
    with pytest.raises(ValueError, match=msg):
        Categorical(['a', 'b'], categories=['a', 'b'], dtype=dtype)
    with pytest.raises(ValueError, match=msg):
        Categorical(['a', 'b'], ordered=True, dtype=dtype)
    with pytest.raises(ValueError, match=msg):
        Categorical(['a', 'b'], ordered=False, dtype=dtype)