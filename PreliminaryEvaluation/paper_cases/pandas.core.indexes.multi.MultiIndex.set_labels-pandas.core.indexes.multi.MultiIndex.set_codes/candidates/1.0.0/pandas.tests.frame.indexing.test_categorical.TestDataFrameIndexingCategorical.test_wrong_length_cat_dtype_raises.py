def test_wrong_length_cat_dtype_raises(self):
    cat = pd.Categorical.from_codes([0, 1, 1, 0, 1, 2], ['a', 'b', 'c'])
    df = pd.DataFrame({'bar': range(10)})
    err = 'Length of values does not match length of index'
    with pytest.raises(ValueError, match=err):
        df['foo'] = cat