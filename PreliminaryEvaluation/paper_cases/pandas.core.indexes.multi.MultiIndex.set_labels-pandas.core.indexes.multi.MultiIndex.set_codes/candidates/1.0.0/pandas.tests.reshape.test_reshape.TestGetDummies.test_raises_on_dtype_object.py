def test_raises_on_dtype_object(self, df):
    with pytest.raises(ValueError):
        get_dummies(df, dtype='object')