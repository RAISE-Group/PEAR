@pytest.mark.parametrize('df1_vals, df2_vals', [(Series([1, 2], dtype='uint64'), ['a', 'b', 'c']), (Series([1, 2], dtype='int32'), ['a', 'b', 'c']), ([0, 1, 2], ['0', '1', '2']), ([0.0, 1.0, 2.0], ['0', '1', '2']), ([0, 1, 2], ['0', '1', '2']), (pd.date_range('1/1/2011', periods=2, freq='D'), ['2011-01-01', '2011-01-02']), (pd.date_range('1/1/2011', periods=2, freq='D'), [0, 1]), (pd.date_range('1/1/2011', periods=2, freq='D'), [0.0, 1.0]), (pd.date_range('20130101', periods=3), pd.date_range('20130101', periods=3, tz='US/Eastern'))])
def test_merge_incompat_dtypes_error(self, df1_vals, df2_vals):
    df1 = DataFrame({'A': df1_vals})
    df2 = DataFrame({'A': df2_vals})
    msg = 'You are trying to merge on {lk_dtype} and {rk_dtype} columns. If you wish to proceed you should use pd.concat'.format(lk_dtype=df1['A'].dtype, rk_dtype=df2['A'].dtype)
    msg = re.escape(msg)
    with pytest.raises(ValueError, match=msg):
        pd.merge(df1, df2, on=['A'])
    msg = 'You are trying to merge on {lk_dtype} and {rk_dtype} columns. If you wish to proceed you should use pd.concat'.format(lk_dtype=df2['A'].dtype, rk_dtype=df1['A'].dtype)
    msg = re.escape(msg)
    with pytest.raises(ValueError, match=msg):
        pd.merge(df2, df1, on=['A'])