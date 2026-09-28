def test_dataframe_dummies_prefix_sep_bad_length(self, df, sparse):
    with pytest.raises(ValueError):
        get_dummies(df, prefix_sep=['bad'], sparse=sparse)