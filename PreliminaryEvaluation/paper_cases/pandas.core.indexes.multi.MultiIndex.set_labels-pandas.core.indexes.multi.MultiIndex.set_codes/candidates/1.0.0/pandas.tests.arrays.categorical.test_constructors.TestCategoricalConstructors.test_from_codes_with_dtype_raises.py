def test_from_codes_with_dtype_raises(self):
    msg = 'Cannot specify'
    with pytest.raises(ValueError, match=msg):
        Categorical.from_codes([0, 1], categories=['a', 'b'], dtype=CategoricalDtype(['a', 'b']))
    with pytest.raises(ValueError, match=msg):
        Categorical.from_codes([0, 1], ordered=True, dtype=CategoricalDtype(['a', 'b']))