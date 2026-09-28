def test_grouping_error_on_multidim_input(self, df):
    msg = "Grouper for '<class 'pandas.core.frame.DataFrame'>' not 1-dimensional"
    with pytest.raises(ValueError, match=msg):
        Grouping(df.index, df[['A', 'A']])