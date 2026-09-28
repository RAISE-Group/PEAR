def test_dataframe_dummies_prefix_bad_length(self, df, sparse):
    with pytest.raises(ValueError):
        get_dummies(df, prefix=['too few'], sparse=sparse)