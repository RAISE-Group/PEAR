def test_usecols_int(self, read_ext, df_ref):
    df_ref = df_ref.reindex(columns=['A', 'B', 'C'])
    msg = 'Passing an integer for `usecols`'
    with pytest.raises(ValueError, match=msg):
        with ignore_xlrd_time_clock_warning():
            pd.read_excel('test1' + read_ext, 'Sheet1', index_col=0, usecols=3)
    with pytest.raises(ValueError, match=msg):
        with ignore_xlrd_time_clock_warning():
            pd.read_excel('test1' + read_ext, 'Sheet2', skiprows=[1], index_col=0, usecols=3)